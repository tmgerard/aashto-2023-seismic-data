# AASHTO 2023 Seismic Data
With the release of the latest [AASHTO Guide Specifications for LRFD Bridge Seismic Design, 3rd Edition](https://store.transportation.org/item/collectiondetail/251) a new seismic design reponse spectrum model is required. The new response spectrum is built from a series of 22 data points that are available in the AASHTO-USGS Seismic Design Ground Motion Database. AASHTO Guide Specification Article 3.4.1 states the following:

> *Risk-targeted design response spectra shall be constructed using response spectral accelerations taken from the AASHTO–USGS Seismic Design Ground Motion Database developed by the USGS using the 2018 NSHM, as described in this Article.*
>
> *The ground motion database provides 5 percent damped design acceleration coefficients, Sa, at 22 different periods as follows: 0 s (As), 0.01, 0.02, 0.03, 0.05, 0.075, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.5, and 10 s.*
>
> *The design response spectrum shall be constructed directly using these values, with linear interpolation between the provided values. For periods greater than 10 seconds, the design acceleration coefficients shall be determined by a site-specific, risk-targeted seismic hazard analysis.*

This program provides a simple user interface that allows a user to create retrive data from the [AASHTO 2023 Web Service](https://earthquake.usgs.gov/ws/designmaps/aashto-2023/) and display the data in a format that is helpful for a structural engineer.

![Program gif](/docs//python-usgs-aashto-2023-app.gif)

## How it Works
The program uses the latitude, longitude, and soil site classification provided by the user to construct a web query following the [AASHTO 2023 Web Service](https://earthquake.usgs.gov/ws/designmaps/aashto-2023/) documentation. If the query is successful, the program uses the information in the retrieved JSON file to construct a graph and provide data points that that can be copied into another program, such as a dynamic analysis program to analyze a structures earthquake response.

## Set Up
The program uses several libraries for the program interface, output, testing, and deployment.

- [ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/installation/)
- [matplotlib](https://matplotlib.org/stable/users/installing/index.html)
- [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html)
- [PyInstaller](https://pyinstaller.org/en/stable/)

The following pacakges can be installed using pip in the command line.

``python -m pip install ttkbootstrap``

``python -m pip install matplotlib``

``python -m pip install pytest``

To package the file up for deployment to those who may want the program as a standalone application.

 - install pyinstaller

``python -m pip install pyinstaller``

 - install the packages locally, running pip from the project folder so pyinstaller will package it into the executable properly
  
  `` pip install .``

 - package the program using pyinstaller

 `` pyinstaller -F --noconsole main.py``

