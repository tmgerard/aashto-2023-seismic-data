import tkinter as tkinter
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from AASHTO2023Data import Config_AASHTO2023


class SeismicInputFrame(ttkb.Frame):
    """
    A frame containing the inputs for building the web query for the AASHTO 2023 Ground
    Motion Data
    """
    def __init__(self, master, config: Config_AASHTO2023) -> None:
        super().__init__(master)
        self.__config = config
        self.__add_entries()
    
    def __add_entries(self):
        self.lat_label = ttkb.Label(self, bootstyle=DEFAULT, text='Latitude')
        self.lat_label.grid(row=0, column=0, padx=5, pady=(0, 5), sticky='e')

        self.lat_entry = ttkb.Entry(self, bootstyle=DEFAULT)
        self.lat_entry.grid(row=0, column=1, padx=5, pady=(0, 5), sticky='ew')

        self.long_label = ttkb.Label(self, bootstyle=DEFAULT, text='Longitude')
        self.long_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

        self.long_entry = ttkb.Entry(self, bootstyle=DEFAULT)
        self.long_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        self.site_class_label = ttkb.Label(self, bootstyle=DEFAULT, text='Soil Classfication')
        self.site_class_label.grid(row=2, column=0, padx=5, pady=(5, 0), sticky='e')

        self.site_class_combo = ttkb.Combobox(self, bootstyle=DEFAULT, values=self.__config.allowable_site_classes)
        self.site_class_combo.grid(row=2, column=1, padx=5, pady=(5, 0), sticky='ew')
        self.site_class_combo.current(3)
    