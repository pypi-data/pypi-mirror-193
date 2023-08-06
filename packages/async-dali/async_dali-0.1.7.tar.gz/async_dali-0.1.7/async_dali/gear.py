from dataclasses import dataclass
from enum import Enum
from typing import Any, NamedTuple

from .address import AbstractDaliAddress, DaliGearGroupAddress
from .dali_alliance_db import DaliAllianceProductDB, DaliAllianceProductRecord
from .types import DaliCommandCode, DaliException, SpecialCommandCode


class Fade(NamedTuple):
    """
    Fade rate
    1: 358 steps/sec
    2. 253 steps/sec
    3. 179 steps/sec
    4. 127
    5. 89 
    6. 63
    7. 45 
    8. 32
    9. 22
    10. 16
    11. 11.2
    12. 7.9
    13. 5.6
    14. 4.0
    15. 2.8
    """

    """
    Fade Time
    0: < 0.7sec
    1: 0.7
    2. 1
    3. 1.4
    4. 2 
    5. 2.8
    6. 4
    7. 5.6
    8. 8
    9. 11.3 
    10. 16
    11. 22.6
    12. 32
    13. 45.2
    14. 64
    15. 90.5 seconds

    """
    time: int
    rate: int


class GearType(Enum):
    FLOURESCENT_LAMP = 0
    EMERGENCY_LIGHTING = 1
    HID_LAMP = 2
    LOW_VOLTAGE_HALOGEN_LAMP = 3
    INCANDESCENT_LAMP_DIMMER = 4
    DC_CONTROLLED_DIMMER = 5
    LED_LAMP = 6
    RELAY = 7
    COLOUR = 8

    GEAR_GROUP = 128  # This isn't a DALI GearType.  Its a magic value we put in for Groups. 


@dataclass
class DaliGear:
    # The main fields that must be set at construction time.
    transciever: Any  # To avoid circular dependency
    address: AbstractDaliAddress

    # Device state
    level: int = 0
    groups: int = 0

    # Device info that we read from memory bank 0 - These won't be populated until update_all is called
    device_type: GearType|None = None
    dalidb_record: DaliAllianceProductRecord|None = None
    last_mem_bank: int = 0
    gtin: int = 0
    firmware_version: str|None = None
    serial: str|None = None
    hardware_version: str|None = None
    dali_version: int = 0
    device_num_logical_control_units: int = 0
    device_num_logical_control_gears: int = 0
    device_control_index: int = 0
    fade: Fade |None  = None
    power_on_level: int = -1


    def __init__(self, transciever: Any, address: AbstractDaliAddress) -> None:
        self.transciever = transciever
        self.address = address

    @property
    def unique_id(self):
        """
        DALI defines the combination of GTIN and serial number to be globally unique and immutable, but
        a single physical device might consist of multiple logical devices, so we add that too
        """
        if self.device_type is None:
            raise DaliException("Device info not fetched")
        return "{}-{}-{}".format(self.gtin, self.serial, self.device_control_index)


    async def _send_cmd(self, cmd, repeat=1):
        return await self.transciever.send_cmd(self.address, cmd, repeat)

    async def read_memory(self, bank, offset, num):
        await self.transciever.send_special_cmd(SpecialCommandCode.SetDTR1, bank)  # Set memory bank
        await self.transciever.send_special_cmd(SpecialCommandCode.SetDTR0, offset)  # Set location 

        buf = bytearray()
        for i in range(num):
            b =  await self.transciever.send_cmd(self.address, DaliCommandCode.ReadMemoryLocation)
            if b is None:
                raise Exception("got no response when querying memory")
            buf.append(b)
        return bytes(buf)

    @property
    def present(self): 
        return self.device_type is not None

    async def update_all(self):
        await self.update_deviceinfo()
        if self.present:
            await self.update_groups()
            await self.update_brightness_range()
            await self.update_level()
            await self.update_fade()
            await self.update_power_on_level()

    async def update_deviceinfo(self):
        """Reads device information, including the device type, GTIN and product code from memory bank 0 """
        dt = await self.transciever.send_cmd(self.address, DaliCommandCode.QueryDeviceType)
        if dt is None:
            self.device_type = None
        else:
            self.device_type = GearType(dt)
        if self.device_type is not None:
            # Read information on the bank 0 of the device
            # See https://infosys.beckhoff.com/english.php?content=../content/1033/tcplclib_tc3_dali/6940982539.html&id= for details on the memory banks
            # Returns the content of the memory location stored in DTR0 that is located within the memory bank listed in DTR1
            buf = await self.read_memory(0, 2, 25)

            '''
            Example DALI data (from index 02 onwards. )
            LMB GTIN        VER  SER Major  SER MI HWV  DALI VERSION
            01 07ee4bb3b889 0707 00001a5838 920269 0300 08 

            GTIN can be looked up by screen scraping (see dali_alliance_db.py)
            '''

            self.gtin = int.from_bytes(buf[1:7], "big")
            self.last_mem_bank = buf[0],
            self.firmware_version = "{}.{}".format(buf[7],buf[8]),
            self.serial = "{:02x}{:02x}{:02x}{:02x}{:02x}.{:02x}{:02x}{:02x}".format(buf[13],buf[12],buf[11],buf[10],buf[9],buf[16],buf[15],buf[14])
            self.hardware_version = "{}.{}".format(buf[17], buf[18]),
            self.dali_version = buf[19]

            self.device_num_logical_control_units = buf[22]
            self.device_num_logical_control_gears = buf[23]
            self.device_control_index = buf[24]

            with DaliAllianceProductDB() as db:
                self.dalidb_record = await db.fetch(self.gtin)

    async def update_brightness_range(self): 
        """Updates the range of brightness allowed for this device"""
        self.min_level = await self._send_cmd(DaliCommandCode.QueryMinLevel)
        self.max_level = await self._send_cmd(DaliCommandCode.QueryMaxLevel)
        return (self.min_level, self.max_level)

    async def update_groups(self): 
        """Updates the groups that this device is a member of"""
        g0 = await self._send_cmd(DaliCommandCode.QueryGroupsZeroToSeven)
        g1 = await self._send_cmd(DaliCommandCode.QueryGroupsEightToFifteen)
        self.groups = g1 << 8 | g0
        return self.groups

    async def update_level(self): 
        """Updates the current brightness level for this device.  0 is off, all other values are on the DALI logarithmic scale"""
        self.level = await self._send_cmd(DaliCommandCode.QueryActualLevel)
        return self.level

    async def update_fade(self):
        fade_and_rate =  await self._send_cmd(DaliCommandCode.QueryFadeTimeFadeRate)
        self.fade = Fade(time = fade_and_rate >> 4, rate = fade_and_rate & 0x0F)
        return self.fade


    async def update_power_on_level(self):
        """Determine the power on level of this device"""
        self.power_on_level =  await self._send_cmd(DaliCommandCode.QueryPowerOnLevel)
        return self.power_on_level


    async def brightness(self, level):
        """Sets the brightness to a specific power level, via the DAPC command"""
        await self.transciever.send_direct_arc_power(self.address, level)
        # self.level = level

    async def add_to_group(self, group: int):
        """Sets the brightness to a specific power level, via the DAPC command"""
        
        if group < 0 or group > 15:
            raise ValueError("Group number must be between 0 and 15 inclusive")
        await self._send_cmd(DaliCommandCode(DaliCommandCode.AddToGroup0.value + group), repeat=2)
        # self.level = level

    async def remove_from_group(self, group: int):
        """Sets the brightness to a specific power level, via the DAPC command"""
        
        if group < 0 or group > 15:
            raise ValueError("Group number must be between 0 and 15 inclusive")
        await self._send_cmd(DaliCommandCode(DaliCommandCode.RemoveFromGroup0.value + group), repeat=2)


    async def on(self):
        """Turns the light on - to wherever it was last time it was on"""
        # For the LED ballasts I'm using, Sending the ON command doesn't seem to work.  Instead, we recall the last active level (could also be recall Max level)
        await self._send_cmd(DaliCommandCode.GoToLastActiveLevel)

    async def max(self):
        """Turns the light on at its maximum brightness"""
        # For the LED ballasts I'm using, Sending the ON command doesn't seem to work.  Instead, we recall the last active level (could also be recall Max level)
        await self._send_cmd(DaliCommandCode.RecallMaxLevel)

    async def min(self):
        """Turns the light on at its minimum brightness"""
        # For the LED ballasts I'm using, Sending the ON command doesn't seem to work.  Instead, we recall the last active level (could also be recall Max level)
        await self._send_cmd(DaliCommandCode.RecallMinLevel)




    async def off(self):
        """Turns the light off"""
        await self._send_cmd(DaliCommandCode.Off)

    async def brighten(self):
        """If possible, instructs the device to get brighter"""
        await self._send_cmd(DaliCommandCode.Up)

    async def dim(self):
        """If possible, instructs the device to get dimmer"""
        await self._send_cmd(DaliCommandCode.Down)


    async def set_power_on_level(self, level):
        """Change the power on level of this device"""
        await self.transciever.send_special_cmd(DaliCommandCode.SetDTR0, level)
        await self._send_cmd(DaliCommandCode.SetPowerOnLevel, 2)


    async def toggle(self):
        """If the light is off, turn it on.  If it is on, turn it off"""
        if self.level == 0:
            await self.on()
        else:
            await self.off()



class DaliGearGroup(DaliGear):
    def __init__(self, transciever, address: DaliGearGroupAddress) -> None:
        super().__init__(transciever, address)
        if not isinstance(address, DaliGearGroupAddress):
            raise Exception("Invalid Address Argument")

    @property
    def unique_id(self):
        """
        Unique IDs for a DaliGearGroup are a bit different, as they are tied to the bus on which they exist.
        """
        return "{}-{}".format(self.transciever.unique_id, self.address)

    @property
    def mask(self):
        """The mask (bit shifted position) of the group, used for matching against device group bitmasks"""
        return 1 << self.address.group_num

    @property
    def has_gear(self):
        """Returns True if this group has 1 or more members in it"""
        return len(self.group_members()) > 0

    def group_members(self):
        """Checks all of our gear's group membership, and return those that are in this group"""
        mask = self.mask
        return [gear for gear in self.transciever.devices if gear.groups & mask != 0]

    async def update_deviceinfo(self):
        """Groups don't have device info, so we override to just use whatever the first member's values are."""
        self.device_type = GearType.GEAR_GROUP
        self.groups = 0
        members = self.group_members()
        if len(members) > 0:
            first = members[0]
            self.max_level = first.max_level
            self.min_level = first.min_level
        else:
            self.max_level = 254
            self.min_level = 1

    async def update_level(self): 
        """Instead of querying all of the gear, we query the first member of this group (assuming there is one)"""
        members = self.group_members()
        if len(members) == 0:
            self.level = 0
        else:            
            self.level = members[0].level
        return self.level

    async def update_brightness_range(self): 
        members = self.group_members()
        if len(members) == 0:
            return (1,254)
        else:            
            self.min_level = members[0].min_level
            self.max_level = members[0].max_level
        return (self.min_level, self.max_level)

    async def update_groups(self): 
        """Groups by definition don't have groups"""
        return self.groups

    async def update_fade(self):
        members = self.group_members()
        if len(members) == 0:
            return None
        else:            
            self.fade = members[0].fade
        return self.fade


    async def update_power_on_level(self):
        members = self.group_members()
        if len(members) == 0:
            return 0
        else:            
            self.power_on_level = members[0].power_on_level
        return self.power_on_level
