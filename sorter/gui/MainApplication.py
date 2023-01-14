import tkinter as tk

from logic.Logger import Logger
from logic.Sorter import Sorter

from .ConfigCreator import ConfigCreator
from logic.BaseComponent import BaseComponent

from logic.Mediator import SorterMediator

WIDTH = 600
HEIGHT = 600
POS_X = 300
POS_Y = 200


class MainApplication(tk.Frame, BaseComponent):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # root
        self.parent = parent

        self._setup_size_and_positioning()
        self._setup_layout()
        self._setup_widgets()
        self._setup_mediator()

    def _setup_size_and_positioning(self) -> None:
        self.winfo_toplevel().title("File sorter")
        self.winfo_toplevel().geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
        self.config(width=WIDTH, height=HEIGHT)

    def _setup_layout(self) -> None:
        self.grid(row=0, column=0)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

    def _setup_widgets(self) -> None:
        self.cfg = ConfigCreator(self)
        self.cfg.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.run_btn = tk.Button(self, text="Run script",command=self._run_script)
        self.run_btn.place(relx=0.33, rely=0.9)

        self.stop_btn = tk.Button(self, text="Stop script", command=self._stop_script)
        self.stop_btn.place(relx=0.53, rely=0.9)
        self.stop_btn.config(state='disabled')
    
    def _setup_mediator(self) -> SorterMediator:
        logger: Logger = Logger()
        sorter: Sorter = Sorter()
        mediator: SorterMediator = SorterMediator(self, self.cfg, logger, sorter)
        return mediator

    def _run_script(self) -> None:
        self.stop_btn.config(state='active')
        self.run_btn.config(state='disabled')
        pass
    
    def _stop_script(self) -> None:
        self.stop_btn.config(state='disabled')
        self.run_btn.config(state='active')
        pass


