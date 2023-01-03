import os
import traceback

from typing import Optional, Type
from types import TracebackType

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(metaclass=Singleton):

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
            
    def create_logfile(self, logfile_name: str) -> str:
        if not os.path.isdir("./logs"):
            os.mkdir("./logs")
        logfile_path: str = f"./logs/{logfile_name}.txt"
        open(logfile_path, 'a').close()
        return logfile_path

    