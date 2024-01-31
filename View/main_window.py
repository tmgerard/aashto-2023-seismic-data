import tkinter as tkinter
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

from View.input_frame import SeismicInputFrame
from View.output_frame import SeismicOutputFrame
from View.graph_frame import SeismicGraphFrame
from AASHTO2023Data import Config_AASHTO2023, QueryBuilder_AASHTO2023, SeismicData_AASHTO2023, get_aashto_ground_motion_data, UsgsStatusErrorException


class AASHTO2023Main(ttkb.Window):
    def __init__(self, config: Config_AASHTO2023, title="AASHTO 2023 Ground Motion Data", themename="litera", 
                 iconphoto='', size=None, position=None, minsize=None, 
                 maxsize=None, resizable=None, hdpi=True, scaling=None, 
                 transient=None, overrideredirect=False, alpha=1):
        
        super().__init__(title, themename, iconphoto, size, 
                         position, minsize, maxsize, resizable, 
                         hdpi, scaling, transient, overrideredirect, alpha)
        
        self.__config = config
        self.__add_input_frame()
        self.__add_output_frame()
        self.__add_button()
        self.__add_graph()
        self.__add_status_label()
    
    def __add_input_frame(self) -> None:
        self.input_frame = SeismicInputFrame(self, self.__config)
        self.input_frame.grid(row=0, column=0, padx=5, pady=(15, 5), sticky=tkinter.NSEW)
    
    def __add_output_frame(self) -> None:
        self.output_frame = SeismicOutputFrame(self)
        self.output_frame.grid(row=1, column=0, padx=5, pady=0, sticky=tkinter.NSEW)
        self.grid_rowconfigure(1, weight=1)
    
    def __add_button(self):
        self.retrieve_button = ttkb.Button(self, bootstyle=DEFAULT, text='Get Seismic Data', command=self.__button_click)
        self.retrieve_button.grid(row=2, column=0, sticky=tkinter.EW, padx=(5, 5), pady=(10, 5))

    def __add_status_label(self):
        self.status_label = ttkb.Label(self, bootstyle=DEFAULT, text='', anchor=CENTER)
        self.status_label.grid(row=3, column=0, columnspan=3, padx=(15, 5), pady=5, sticky=tkinter.W)

    def __add_graph(self):
        self.graph = SeismicGraphFrame(self)
        self.graph.grid(row=0, column=2, rowspan=3, padx=20, pady=15, sticky=tkinter.NSEW)

    def __button_click(self):
        try:
            if self.input_frame.lat_entry.get().strip() == '':
                raise ValueError('A latitude value must be entered')
            if self.input_frame.long_entry.get().strip() == '':
                raise ValueError('A longitude value must be entered')
            
            builder = QueryBuilder_AASHTO2023(self.__config)
            query_string = builder.build_query(
                self.input_frame.lat_entry.get().strip(),
                self.input_frame.long_entry.get().strip(),
                self.input_frame.site_class_combo.get().strip()
                )
            self.seismic_data = SeismicData_AASHTO2023(get_aashto_ground_motion_data(query_string))
            self.status_label.config(text='Data Retrieved Successfully', bootstyle=SUCCESS)
            self.output_frame.update(self.seismic_data)
            self.graph.plot(self.seismic_data)
        except ValueError as e:
            self.status_label.config(text='Value Error: {0}'.format(e), bootstyle=DANGER)
        except UsgsStatusErrorException:
            self.status_label.config(text='Response Error: {0}'.format(e), bootstyle=WARNING)
        except Exception as e:
            self.status_label.config(text='Unknown Error: {0}'.format(e), bootstyle=DANGER)
