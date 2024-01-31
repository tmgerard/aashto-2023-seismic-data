import tkinter as tkinter
from ttkbootstrap.constants import *
from AASHTO2023Data.aashto_2023_config import Config_AASHTO2023
from View.main_window import AASHTO2023Main

if __name__ == '__main__':
    
    config = Config_AASHTO2023(r'AASHTO2023Data\seismic_query.json')
    root = AASHTO2023Main(config, themename='superhero')
    root.mainloop()
