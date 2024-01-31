import urllib.request
import json


def get_aashto_ground_motion_data(query_url: str) -> dict:
    """
    Retrieve AASHTO 2023 Risk-Targetd ground motion data from the USGS
    website (https://earthquake.usgs.gov/ws/designmaps/aashto-2023/) given
    a properly formatted query string

    /ws/designmaps/aashto-2023/spectra/{longitude}/{latitude}/{siteClass}?format=JSON
    
    -or-
    
    /ws/designmaps/aashto-2023/spectra/{longitude}/{latitude}/{siteClass}?format=CSV
    """
    with urllib.request.urlopen(query_url) as url:
        data = json.loads(url.read().decode())

    if data['status'] == 'error':
        raise UsgsStatusErrorException
    
    return data

class UsgsStatusErrorException(Exception):
    """
    Exception to raise when the USGS web query returns an error status
    """
    def __init__(self, message='The USGS website could not provide data for the given coordinates'):
        super().__init__(message)