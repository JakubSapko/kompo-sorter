from abc import ABC
from enum import Enum

class EVENTS(Enum):
    CFG_ADD = 'Config add'
    CFG_REM = 'Config remove'
    EXP = 'Config exported'
    IMP = 'Config imported'
    START = 'App start'
    END = 'App end'


class Mediator(ABC):
    '''
    Mediator interface defining a notify method
    '''
    def notify(self, sender: object, event: str, **kwargs) -> None:
        pass

class SorterMediator(Mediator):
    def __init__(self, gui, cfg, logger, sorter) -> None:
        self._gui = gui
        self._gui.mediator = self

        self._cfg = cfg
        self._cfg.mediator = self

        self._logger = logger
        self._logger.mediator = self

        self._sorter = sorter
        self._sorter.mediator = self
    
    def notify(self, sender: object, event: str, **kwargs) -> None:
        data = kwargs
        print(f"keywordy w mediatorze {data=}")
        if event == EVENTS.CFG_ADD:
            self._logger.log(f"{sender}: Added {data['new_rule']} to config")
        if event == EVENTS.CFG_REM:
            self._logger.log(f"{sender}: Removed {data['removed_rule']} to config")
        if event == EVENTS.EXP:
            self._logger.log(f"{sender}: Exported config to {data['export_source']}")
        if event == EVENTS.IMP:
            self._logger.log(f"{sender}: Imported config from {data['config_src']}")
        if event == EVENTS.START:
            self._logger.log(f"{sender}: App started running")
        if event == EVENTS.END:
            self._logger.log(f"{sender}: App stopped running")