from tkinter import Listbox, StringVar, Entry, Label, Button, filedialog
import tkinter as tk

DEFAULT_PADDING_TOP = 15
DEFAULT_PADDING_BOTTOM = 5
DEFAULT_PADDING_LEFT = 10
DEFAULT_PADDING_RIGHT = 0


class ConfigCreator(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self._setup_widgets()

    def _setup_widgets(self) -> None:

        # Directory name setup
        dir_name: str = StringVar()
        dir_name_label: Label = Label(self, text="Provide a directory to config")
        dir_name_label.grid(column=0, row=2, padx=(10, 0))
        dir_name_entry: Entry = Entry(self, textvariable=dir_name)
        dir_name_entry.grid(
            column=0,
            row=6,
            rowspan=3,
            padx=(DEFAULT_PADDING_LEFT, DEFAULT_PADDING_RIGHT),
            pady=(DEFAULT_PADDING_TOP, DEFAULT_PADDING_BOTTOM),
        )

        # Directory extensions setup
        dir_extensions: str = StringVar()
        dir_extensions_label: Label = Label(
            self, text="Provide extensions for a given directory"
        )
        dir_extensions_label.grid(column=0, row=9, padx=(10, 0))
        dir_extensions_entry: Entry = Entry(self, textvariable=dir_extensions)
        dir_extensions_entry.grid(
            column=0,
            row=10,
            rowspan=3,
            padx=(DEFAULT_PADDING_LEFT, DEFAULT_PADDING_RIGHT),
            pady=(DEFAULT_PADDING_TOP, DEFAULT_PADDING_BOTTOM),
        )

        # Submit button setup
        submit_button: Button = Button(self, text="Submit")
        submit_button.grid(
            column=0, row=13, pady=(DEFAULT_PADDING_TOP, DEFAULT_PADDING_BOTTOM)
        )

        # Config list setup
        countrynames = (
            "Argentina",
            "Australia",
            "Belgium",
            "Brazil",
            "Canada",
            "China",
            "Denmark",
            "Finland",
            "France",
            "Greece",
            "India",
            "Italy",
            "Japan",
            "Mexico",
            "Netherlands",
            "Norway",
            "Spain",
            "Sweden",
            "Switzerland",
        )
        cnames = StringVar(value=countrynames)
        conifg_listbox: Listbox = Listbox(self, listvariable=cnames, height=6)
        conifg_listbox.grid(column=0, row=14, rowspan=6)

        # Export config setup
        export_config_button: Button = Button(
            self, text="Export config", command=self.export_config
        )
        export_config_button.grid(
            column=0, row=20, pady=(DEFAULT_PADDING_TOP, DEFAULT_PADDING_BOTTOM)
        )
        # Import config setup
        import_config_button: Button = Button(
            self, text="Import config", command=self.import_config
        )
        import_config_button.grid(
            column=0, row=21, pady=(DEFAULT_PADDING_TOP, DEFAULT_PADDING_BOTTOM)
        )
        # imported_config = filedialog.askopenfile()

    def import_config(self) -> None:
        filedialog.askopenfile()

    def export_config(self) -> None:
        filedialog.asksaveasfilename()
