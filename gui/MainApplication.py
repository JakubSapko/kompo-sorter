import tkinter as tk
from typing import NoReturn

from components.Main import Main

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.main = Main(self, bg="red")
        self.main.pack(side="right", fill="both", expand=True)
        self._setup_size_and_positioning()

    def _setup_size_and_positioning(self) -> NoReturn:
        self.winfo_toplevel().title('File sorter')
        self.winfo_toplevel().geometry("800x600+300+200")

        

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()