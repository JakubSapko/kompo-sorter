import pathlib
import os
from os.path import isfile, join
import shutil
from .BaseComponent import BaseComponent
from .Mediator import EVENTS
from .Timer import RepeatingTimer

class FileHandler(BaseComponent):
    def __init__(self) -> None:
        self.is_running = False
        # Desktop path
        self.path = pathlib.Path.home() / 'Desktop'
        self.other_path = self._setup_other()
        self.go_recursively = True
    
    def _setup_other(self) -> None:
        if not os.path.exists(f"{self.path}/Other"):
            os.makedirs(f"{self.path}/Other")
        return f"{self.path}/Other"

    def _load_config(self, cfg) -> None:
        self.cfg = cfg

    def _create_destination_string(self, file: str) -> str | None:
        file_extension: str = file.split('.')[1]
        file_destination: str | None = self.cfg.get(f".{file_extension}", None)
        return file_destination

    def _sort(self) -> None:
        files_when_run: list[str] = [join(self.path, f) for f in os.listdir(self.path) if isfile(join(self.path, f))]
        for file in files_when_run:
            self._sort_file(file)


    def _sort_file(self, file: str) -> None:
        file_destination: str  | None= self._create_destination_string(file)
        if file_destination is None:
            try:
                shutil.copy2(file, self.other_path)
                os.remove(file)
            except shutil.SameFileError:
                self.mediator.notify('FileHandler', EVENTS.E_MOVE, file=file)
            return
        if not os.path.exists(f"{self.path}/{file_destination}"):
            os.makedirs(f"{self.path}/{file_destination}")
        dest: str = join(self.path, file_destination)
        try:
            shutil.copy2(file, dest)
            os.remove(file)
        except shutil.SameFileError:
                self.mediator.notify('FileHandler', EVENTS.E_MOVE, file=file)
        self.mediator.notify('FileHandler', EVENTS.MOVE, file=file, destination=dest)

    def run_sort(self) -> None:
        print(f"{self.cfg=}")
        #presort
        self._sort()
        self.is_running = True
        self.rt = RepeatingTimer(10, self._sort)
    
    def stop_sort(self) -> None:
        self.rt.stop()
        self.is_running = False