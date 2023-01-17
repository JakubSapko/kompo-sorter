from abc import ABC
from enum import Enum
from typing import Dict

class EVENTS(Enum):
    CFG_ADD = 'Config add'
    CFG_REM = 'Config remove'
    EXP = 'Config exported'
    IMP = 'Config imported'
    START = 'App start'
    END = 'App end'
    MOVE = 'File moved by sorter'
    E_MOVE = 'Error when moving'
    FILE_CREATE = 'File created'
    FILE_MOVE = 'File was moved'


class Mediator(ABC):
    '''
    Mediator interface defining a notify method
    '''
    def notify(self, sender: object, event: str, **kwargs) -> None:
        pass

class SorterMediator(Mediator):
    def __init__(self, gui, cfg, cfg_handler, logger, sorter) -> None:
        self._gui = gui
        self._gui.mediator = self

        self._cfg = cfg
        self._cfg.mediator = self

        self._cfg_handler = cfg_handler
        self._cfg_handler.mediator = self

        self._logger = logger
        self._logger.mediator = self

        self._sorter = sorter
        self._sorter.mediator = self
    
    def notify(self, sender: object, event: str, **kwargs) -> None:
        data = kwargs
        if event == EVENTS.CFG_ADD:
            self._logger.log(f"{sender}: Added {data['dirname']} : {data['extensions']} to config")
            updated_config: Dict[str, str] = self._cfg_handler.add_to_config(data['dirname'], data['extensions'])
            return updated_config

        if event == EVENTS.CFG_REM:
            self._logger.log(f"{sender}: Removed rule at index {data['index']} from config")
            updated_config: Dict[str, str] = self._cfg_handler.remove_from_config(data['index'])
            return updated_config

        if event == EVENTS.EXP:
            self._logger.log(f"{sender}: Exported config to {data['export_source']}.json")
            self._cfg_handler.save_config(data['export_source'])

        if event == EVENTS.IMP:
            self._logger.log(f"{sender}: Imported config from {data['config_src']}.json")
            imported_config: Dict[str, list[str]] = self._cfg_handler.read_config(data["config_src"])
            return imported_config

        if event == EVENTS.START:
            self._logger.log(f"{sender}: App started running")
            cfg: Dict[str, list[str]] = self._cfg_handler._get_sorting_representation()
            self._sorter._load_config(cfg)
            self._sorter.run_sort()

        if event == EVENTS.END:
            self._logger.log(f"{sender}: App stopped running")
            self._sorter.stop_sort()
        
        if event == EVENTS.MOVE:
            self._logger.log(f"{sender}: Moved file {data['file']} to {data['destination']}")
        
        if event == EVENTS.E_MOVE:
            self._logger.log(f"{sender}: Error when trying to move {data['file']}")
        
        if event == EVENTS.FILE_CREATE:
            self._logger.log(f"{sender}: A new file {data['path']} was created!\n")
            self._sorter._sort_file(data['path'])
        if event == EVENTS.FILE_MOVE:
            self._logger.log(f"{sender}: A file {data['path']} was moved to desktop!\n")
            self._sorter._sort_file(data['path'])