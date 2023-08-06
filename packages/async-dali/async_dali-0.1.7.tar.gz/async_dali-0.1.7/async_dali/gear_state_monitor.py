
from typing import List
from typing import Any
from .bus_transciever import DaliBusTransciever, DaliMessage
from .gear import DaliGear
import logging
import asyncio
import functools


_LOGGER = logging.getLogger(__name__)


class GearStateMonitor:
    """Helper for a specific Transciever. Listens for messages and automatically updates DaliGear state when 
    events that affect them occur.  Once udpates have been done, a callback is """

    def __init__(self, transciever: DaliBusTransciever, listener: Any) -> None:
        if not isinstance(transciever, DaliBusTransciever):
            raise ValueError("Expected Transciever")
        self.transciever = transciever
        self.listener = listener
        # Sequence can be 0 (for external commands) or 1..255 for ones that we send.  We correlate commands and their responses
        # using this array.
        self.outstanding_commands = [None] * 256

    def __enter__(self):
        self.open()

    async def __aenter__(self):
        self.open()


    def open(self):
        self.transciever.add_message_callback(self.on_message)


    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    async def __aexit__(self, exc_type, exc_value, traceback):
        self.close()


    def close(self):
        self.transciever.remove_message_callback(self.on_message)


    async def call_attribute_updater(self, gear: DaliGear, attribute: str) -> None:
        method_name = "update_{}".format(attribute)
        try:
            method = getattr(gear.__class__, method_name)
            return await method(gear)
        except AttributeError:
            _LOGGER.warn("Not calling %s on %s because it doesn't exist", method_name, gear.__class)



    async def _monitor_updates_after_change_task(self, gear, attribute):
        """
        Some commands take a while to take effect (e.g. lights fade at a configured rate), so we check progressively 
        for a period after a change occurs. This gets triggered (as a haas task) by the bus monitor, rather than 
        directly by actions.
        """
        # this needs to be long enough that we capture final state. Be generous.
        for i in range(1,4):
            await asyncio.sleep(i*0.125)
            lvl_before = gear.level
            lvl_after = await self.call_attribute_updater(gear, attribute)
            if lvl_before != lvl_after:
                _LOGGER.debug("Gear %s changed from %s to %s", gear.unique_id, lvl_before, lvl_after)
                self._notify_listener(gear, attribute)
        
    def _notify_listener(self, gear: DaliGear, attribute: str): 
        asyncio.get_event_loop().call_soon(functools.partial(self.listener, gear, attribute))

    async def process_completed_command(self, cmd: DaliMessage, response: DaliMessage):
        affected_gear_and_attribute = cmd.affected_gear
        if affected_gear_and_attribute is not None:
            affected_gear = affected_gear_and_attribute.gear
            attribute = affected_gear_and_attribute.attribute
        
            affected_groups = cmd.get_affected_groups(affected_gear)
            _LOGGER.debug("Gear %s and Groups %s affected attribute %s by %s", affected_gear_and_attribute, affected_groups, attribute, cmd)
            affected_gear.extend(affected_groups)

            loop = asyncio.get_event_loop()
            # Call the appropriate update method on the gear for the changed attribute
            if attribute == "level":
                # Level can change for some time after the command, so we repeatedly check
                for gear in affected_gear:
                    loop.create_task(self._monitor_updates_after_change_task(gear, attribute))
            else:
                # Other attributes take effect immediately, so we may simply update once.
                for gear in affected_gear:
                    await self.call_attribute_updater(gear, attribute)
                    self._notify_listener(gear, attribute)
                
                


    def on_message(self, msg: DaliMessage):
        """
        The transciever sees every command sent on the bus.  Some commands will affect no entities, some will affect
        one entities, and some can affect multiple entities.  To keep the number of changes needed from within HASS to
        a minimum, we determine which entities are changed, if any. For each one that is affected,
        schedule a hass state update.  These changes could have been sent by us or by 3rd party DALI controller devices.
        """

        # We don't notify the listener until we receive a response
        if msg.is_response:
            source_command = self.outstanding_commands[msg.sequence_number]
            if source_command is not None:
                self.outstanding_commands[msg.sequence_number] = None
                asyncio.get_event_loop().create_task(self.process_completed_command(source_command, msg))
                
        else:
            self.outstanding_commands[msg.sequence_number] = msg

