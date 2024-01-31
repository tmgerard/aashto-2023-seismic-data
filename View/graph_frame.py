import tkinter as tkinter
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from matplotlib import pyplot
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from AASHTO2023Data import SeismicData_AASHTO2023


class SeismicGraphFrame(ttkb.Frame):
    """
    A frame containing the inputs for building the web query for the AASHTO 2023 Ground
    Motion Data
    """
    def __init__(self, master) -> None:
        super().__init__(master)
        self.__add_graph()
    
    def __add_graph(self):
        fig = Figure(figsize=(10, 7), dpi=100)
        
        self.spectrum_graph = fig.add_subplot(111)
        self.__set_up_subplot()
        # spectrum_graph.plot(self.seismic_data.x_data, self.seismic_data.y_data)

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()

        self.canvas.get_tk_widget().grid(row=0, column=0)

        self.toolframe = ttkb.Frame(master=self)
        self.toolframe.grid(row=1, column=0, padx=0, pady=0)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolframe)
        self.toolbar.update()

        self.canvas.get_tk_widget().grid(row=0, column=0, sticky='nesw')
    
    def plot(self, seismic_data: SeismicData_AASHTO2023):
        """
        Update plot with given seismic data
        """
        self.spectrum_graph.clear()
        self.__set_up_subplot(seismic_data)
        self.spectrum_graph.plot(seismic_data.x_data, seismic_data.y_data, marker='.')
        self.canvas.draw()
    
    def __set_up_subplot(self, seismic_data: SeismicData_AASHTO2023 = None):
        self.spectrum_graph.set_title('Design Response Spectrum')
        self.spectrum_graph.set_xlabel('Period (s)')
        self.spectrum_graph.set_ylabel('Spectral Acceleration (g)')
        self.spectrum_graph.set_xlim([0, 10])
        self.spectrum_graph.set_xticks(range(0, 11))
        if not seismic_data == None:
            self.spectrum_graph.set_ylim(bottom=0, top=max(seismic_data.y_data) + 0.2)
        self.spectrum_graph.grid()
