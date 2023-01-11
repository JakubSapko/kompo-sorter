from enum import Enum
from tkinter import Listbox, Radiobutton, StringVar, Entry, Label, Button, filedialog
import tkinter as tk


from logic.BaseComponent import BaseComponent
from logic.Mediator import EVENTS

DEFAULT_PADDING_TOP = 15
DEFAULT_PADDING_BOTTOM = 5
DEFAULT_PADDING_LEFT = 10
DEFAULT_PADDING_RIGHT = 0

WIDTH = 800
HEIGHT = 600
POS_X = 300
POS_Y = 200

class Anchor(Enum):
    NORTH = 'n'
    NORTHEAST = 'ne'
    EAST = 'e'
    SOUTHEAST = 'se'
    SOUTH = 's'
    SOUTHWEST = 'sw'
    WEST = 'w'
    NORTHWEST = 'nw'
    CENTER = 'center'

class ConfigCreator(tk.Frame, BaseComponent):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self._setup_widgets()
    def _setup_widgets(self) -> None:

        # Directory name setup
        dir_name: str = StringVar()
        dir_name_label: Label = Label(self, text="Provide a directory to config")
        dir_name_label.place(relx=0.5, rely=0.1, anchor=Anchor.CENTER.value)
        dir_name_entry: Entry = Entry(self, textvariable=dir_name)
        dir_name_entry.place(relx=0.5, rely=0.15, anchor=Anchor.CENTER.value)

        # Directory extensions setup
        dir_extensions: str = StringVar()
        dir_extensions_label: Label = Label(
            self, text="Provide extensions for a given directory"
        )
        dir_extensions_label.place(relx = 0.5, rely=0.2, anchor=Anchor.CENTER.value)
        dir_extensions_entry: Entry = Entry(self, textvariable=dir_extensions)
        dir_extensions_entry.place(relx=0.5, rely= 0.25, anchor=Anchor.CENTER.value)

        # Submit button setup
        submit_button: Button = Button(self, text="Submit")
        submit_button.place(
            relx=0.5, rely=0.30, anchor=Anchor.CENTER.value
        )

        # Config list setup
        config_values = [
            "Example: [.txt,.pdf,.doc]"
        ]
        cnames = StringVar(value=config_values)
        conifg_listbox: Listbox = Listbox(self, listvariable=cnames, height=6, width=40)
        conifg_listbox.place(relx=0.5, rely=0.43, anchor=Anchor.CENTER.value)

        # Export config setup
        export_config_button: Button = Button(
            self, text="Export config", command=self.export_config
        )
        export_config_button.place(
            relx=0.5, rely=0.58, anchor=Anchor.CENTER.value
        )
        # Import config setup
        import_config_button: Button = Button(
            self, text="Import config", command=self.import_config
        )
        import_config_button.place(
            relx=0.5, rely=0.65, anchor=Anchor.CENTER.value
        )
        # imported_config = filedialog.askopenfile()

        # Other files
        other_files_label: Label = Label(
            self, text="What do you want to do with files with other extensions?"
        )
        other_files_label.place(
            relx=0.5, rely=0.7, anchor=Anchor.CENTER.value
        )
        self.other_files_option: StringVar = StringVar()
        skip_option: Radiobutton = Radiobutton(
            self, text="Skip the files", variable=self.other_files_option, value="skip"
        )
        skip_option.place(relx=0.5, rely=0.75, anchor=Anchor.CENTER.value)
        move_to_other_option: Radiobutton = Radiobutton(
            self,
            variable=self.other_files_option,
            text='Move to "Other" directory on your Desktop',
            value="other",
        )
        #Set the default behavior to skipping unrecognized files
        self.other_files_option.set('skip')
        move_to_other_option.place(relx=0.5, rely=0.8, anchor=Anchor.CENTER.value)

    def import_config(self) -> None:
        path = filedialog.askopenfile()
        self.mediator.notify(self, EVENTS.IMP, config_src=path)

    def export_config(self) -> None:
        path = filedialog.asksaveasfilename()
        self.mediator.notify(self, EVENTS.EXP, export_source = path)
