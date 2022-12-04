import tkinter as tk
from components.ConfigCreator import ConfigCreator

WIDTH = 800
HEIGHT = 600
POS_X = 300
POS_Y = 200
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # root

        self._setup_size_and_positioning()
        self._setup_widgets()
        self.cfg.pack(side="left", fill="both", expand=True)
        self.cfgx.pack(side="right", fill="both", expand=True)

    def _setup_size_and_positioning(self) -> None:
        self.winfo_toplevel().title('Test app')
        self.winfo_toplevel().geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
        self.config(width=WIDTH, height=HEIGHT)

    def _setup_widgets(self) -> None:
        self.cfg = ConfigCreator(self)
        self.cfg.config(bg="limegreen")

        self.cfgx = ConfigCreator(self)
        self.cfgx.config(bg="skyblue")
    

        

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()