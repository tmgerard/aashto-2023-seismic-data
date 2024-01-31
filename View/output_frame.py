import tkinter as tk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from AASHTO2023Data import SeismicData_AASHTO2023


class SeismicOutputFrame(ttkb.Frame):
    """
    A frame containing the inputs for building the web query for the AASHTO 2023 Ground
    Motion Data
    """
    def __init__(self, master) -> None:
        super().__init__(master)
        self.__add_entries()
    
    def __add_entries(self):
        self.textbox_label = ttkb.Label(self, text='Graph Data')
        self.textbox_label.pack(fill='x')
        self.textbox = tk.Text(self, width=30, height=30)
        self.textbox.config(state='disabled')
        self.textbox.pack(fill='both')
    
    def update(self, seismic_data: SeismicData_AASHTO2023):
        self.textbox.config(state='normal')
        self.textbox.delete('1.0', tk.END)
        data_text = 'Period (s)\t\tSA (g)\n'
        for i in range(0, len(seismic_data.x_data)):
            data_text += '{0:.4f}\t\t{1:.4f}\n'.format(seismic_data.x_data[i], seismic_data.y_data[i])
        data_text += '\nAs = {0:.4f}\n'.format(seismic_data.spectral_acceleration_as())
        data_text += 'SD1 = {0:.4f}\n'.format(seismic_data.sd1())
        data_text += 'SDs = {0:.4f}\n'.format(seismic_data.sds())
        data_text += '\nSeismic Design Category {0}'.format(seismic_data.seismic_design_category())
        self.textbox.insert(tk.END, data_text)
        self.textbox.config(state='disabled')
