import pytest

from AASHTO2023Data import get_aashto_ground_motion_data
from AASHTO2023Data import SeismicData_AASHTO2023


@pytest.fixture
def seismic_data():
    data = get_aashto_ground_motion_data('https://earthquake.usgs.gov/ws/designmaps/aashto-2023/spectra/-118/34/CD?format=JSON')
    return SeismicData_AASHTO2023(data)


def test_latitude(seismic_data):
    assert seismic_data.latitude == 34.0


def test_longitude(seismic_data):
    assert seismic_data.longitude == -118.0


def test_site_class(seismic_data):
    assert seismic_data.site_class == 'CD'


def test_url(seismic_data):
    assert seismic_data.url == 'https://earthquake.usgs.gov/ws/designmaps/aashto-2023/spectra/-118/34/CD?format=JSON'


def test_x_data(seismic_data):
    # should return a list with 22 data points
    assert len(seismic_data.x_data) == 22


def test_y_data(seismic_data):
    # should return a list with 22 data points
    assert len(seismic_data.y_data) == 22


def test_x_label(seismic_data):
    assert seismic_data.x_label == 'Period (s)'


def test_y_label(seismic_data):
    assert seismic_data.y_label == 'Spectral Acceleration (g)'
