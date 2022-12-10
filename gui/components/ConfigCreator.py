from tkinter import Listbox, StringVar, Entry, Label, Button
import tkinter as tk

class ConfigCreator(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
    
        self._setup_widgets()
    def _setup_widgets(self) -> None:

        # Directory name setup
        dir_name: str = StringVar()
        dir_name_label: Label = Label(self, text="Provide a directory to config")
        dir_name_label.grid(column=0, row=2, padx=(10, 10))
        dir_name_entry: Entry = Entry(self, textvariable=dir_name)
        dir_name_entry.grid(column=0, row=6, rowspan=3, padx=(10, 10), pady=(15, 15))

        # Directory extensions setup
        dir_extensions: str = StringVar()
        dir_extensions_label: Label = Label(self, text="Provide extensions for a given directory")
        dir_extensions_label.grid(column=0, row=9, padx=(10, 10))
        dir_extensions_entry: Entry = Entry(self, textvariable=dir_extensions)
        dir_extensions_entry.grid(column=0, row=10, rowspan=3, padx=(10, 10), pady=(15, 15))

        # Submit button setup
        submit_button: Button = Button(self, text="Submit")
        a
        submit_button.grid(column=0, row=13, pady=(5, 5))
        
        # Config list setup
        # countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
        #     'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
        #     'Sweden', 'Switzerland')
        # cnames = StringVar(value=countrynames)
        # conifg_listbox: Listbox = Listbox(self, listvariable=cnames, height=6)
        # conifg_listbox.grid(column=0, row=10, rowspan=6)
