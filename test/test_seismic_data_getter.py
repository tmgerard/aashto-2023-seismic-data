import pytest

from AASHTO2023Data import get_aashto_ground_motion_data


query = 'https://earthquake.usgs.gov/ws/designmaps/aashto-2023/spectra/-118/34/CD?format=JSON'


def test_get_aashto_ground_motion():
    data = get_aashto_ground_motion_data(query)
    assert data['status'] == 'success'