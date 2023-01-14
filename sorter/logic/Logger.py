import os
import traceback
import sys

import argparse

from typing import Optional, Type, Union
from types import TracebackType

from datetime import datetime


from .BaseComponent import BaseComponent

parser = argparse.ArgumentParser()
parser.add_argument('DEBUG', default=False, nargs='?')
args = parser.parse_args()

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(BaseComponent, metaclass=Singleton):

    # Set this when executing a script using DEBUG=True
    DEBUG = args.DEBUG
    PADDING = 9
    TYPE = {'debug': 'DEBUG',
            'log': 'INFO',
            'exception': 'EXCEPTION',
            'object': 'OBJECT',
            'traceback': 'TRACEBACK'}

    def __init__(self, logfile: str = None, exception_file: str = "errors") -> None:
        self._logfile = self.create_logfile(logfile) if logfile else None
        self._exceptions_file = self.create_logfile(exception_file)

    def __enter__(self):
        log_to = self._logfile if self._logfile else "CMD"
        print(f"Started logging to {log_to}")
    
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], exc_tb: Optional[TracebackType]):
        print("Stopped logging")
        if exc_type or exc_value or exc_tb:
            print(f"Exception of type {exc_type} occured: Exception's value: {exc_value}. Traceback logged to: {self._exceptions_file}. Exiting the script.")
            tb_msg = self._create_log_msg("traceback", " ".join(traceback.format_tb(exc_tb)))
            self.log_to_file(self._exceptions_file, tb_msg)
            
    def _create_log_msg(self, type: str, msg: str) -> str:
        type: str = self.TYPE[type].ljust(self.PADDING)
        now: datetime = datetime.now()
        handled_msg: str = f"|{type}|{now.hour}:{now.minute}|{msg}\n"
        return handled_msg
    
    def _base_log(self, type: str, msg: str) -> Union[str, None]:
        handled_msg: str = self._create_log_msg(type, msg)
        if self._logfile:
            self.log_to_file(self._logfile, handled_msg)
            return
        print(handled_msg)

    def create_logfile(self, logfile_name: str) -> str:
        if not os.path.isdir("./logs"):
            os.mkdir("./logs")
        logfile_path: str = f"./logs/{logfile_name}.txt"
        open(logfile_path, 'a').close()
        return logfile_path

    def log_to_file(self, filename: str, msg: str) -> None:
        with open(filename, 'a') as logfile:
            logfile.write(msg)
    
    def log(self, msg: str) -> None:
        '''
        Basic logging method. Logs as INFO.
        '''
        log_type = sys._getframe().f_code.co_name
        self._base_log(log_type, msg)
    
    def debug(self, msg: str) -> None:
        '''
        Debug logging method. Logs as DEBUG.
        Debug logs should be only called in dev environment and left outside
        of the production environment.
        Enable debug by calling the script with DEBUG flag set to True
        '''
        if not self.DEBUG:
            raise Exception("You can't use debug logs without DEBUG mode set to True")
        log_type = sys._getframe().f_code.co_name
        self._base_log(log_type, msg)

    def exception(self, msg: str) -> None:
        '''
        Exception logging method. Logs as EXCEPTION.
        '''
        log_type = sys._getframe().f_code.co_name
        self._base_log(log_type, msg)
    
    def object(self, obj: object) -> None:
        '''
        Object logging method. Logs as OBJECT.
        Lifted up from log method as those things can get pretty long
        when logged objects get advanced. Requires logged object to have
        a __str__ representation.
        '''
        log_type: str = sys._getframe().f_code.co_name
        obj_msg: str = f"\n--------------\n"\
                        + str(obj)\
                        + f"\n-----------"
        self._base_log(log_type, obj_msg)