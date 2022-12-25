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
        self.parent = parent

        self._setup_size_and_positioning()
        self._setup_layout()
        self._setup_widgets()

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
        cfg = ConfigCreator(self)
        cfg.grid(row=0, column=0, columnspan=2, sticky="nsew")
        cfg.config(bg="limegreen")

        run_btn = tk.Button(self, text="Run script")
        run_btn.place(x = 130, y = 500, width=100, height=25)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
