import tkinter as tk
from typing import NoReturn

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.setup_widgets()

    def setup_widgets(self) -> NoReturn:
        self.winfo_toplevel().title('File sorter')
        self.winfo_toplevel().geometry("800x600+300+200")


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()