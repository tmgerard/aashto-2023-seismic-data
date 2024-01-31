import pytest
from AASHTO2023Data import Config_AASHTO2023


@pytest.fixture
def config():
    return Config_AASHTO2023(r'C:\Users\tmge547\OneDrive - Arkansas Department of Transportation\12 Repos\aashto-2023-seismic-data\AASHTO2023Data\seismic_query.json')

def test_query_template(config):
    assert config.query_template == 'https://earthquake.usgs.gov/ws/designmaps/aashto-2023/spectra/{0}/{1}/{2}'

def test_latitude_min(config):
    assert config.latitude_min == -33.0

def test_latitude_max(config):
    assert config.latitude_max == 72.0

def test_longitude_min(config):
    assert config.longitude_min == -200.0

def test_longitude_max(config):
    assert config.longitude_max == 151.0

def test_allowable_site_classes(config):
    assert config.allowable_site_classes == ["A", "B", "BC", "C", "CD", "D", "DE", "E"]
