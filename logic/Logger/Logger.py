import os


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

    def create_logfile(self, logfile_name: str) -> str:
        if not os.path.isdir("./logs"):
            os.mkdir("./logs")
        logfile_path: str = f"./logs/{logfile_name}.txt"
        open(logfile_path, 'a').close()
        return logfile_path