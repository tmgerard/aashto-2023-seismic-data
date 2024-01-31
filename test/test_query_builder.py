import pytest
from AASHTO2023Data import QueryBuilder_AASHTO2023
from AASHTO2023Data import QueryOutputFormat
from AASHTO2023Data import Config_AASHTO2023

@pytest.fixture
def builder():
    return QueryBuilder_AASHTO2023(
        Config_AASHTO2023(r'C:\Users\tmge547\OneDrive - Arkansas Department of Transportation\12 Repos\aashto-2023-seismic-data\AASHTO2023Data\seismic_query.json')
        )


def test_valid_query_default_JSON(builder):
    assert builder.build_query(34, -118, "CD") == "https://earthquake.usgs.gov/ws/designmaps/aashto-2023/spectra/-118/34/CD?format=JSON"


def test_valid_query_JSON(builder):
    assert builder.build_query(34, -118, "CD", QueryOutputFormat.JSON) == "https://earthquake.usgs.gov/ws/designmaps/aashto-2023/spectra/-118/34/CD?format=JSON"


def test_valid_query_CSV(builder):
    assert builder.build_query(34, -118, "CD", QueryOutputFormat.CSV) == "https://earthquake.usgs.gov/ws/designmaps/aashto-2023/spectra/-118/34/CD?format=CSV"


def test_invalid_query_latitude_too_small(builder):
    with pytest.raises(ValueError):
        builder.build_query(-500, -118, "CD")


def test_invalid_query_latitude_too_big(builder):
    with pytest.raises(ValueError):
        builder.build_query(500, -118, "CD")


def test_invalid_query_longitude_too_small(builder):
    with pytest.raises(ValueError):
        builder.build_query(34, -500, "CD")


def test_invalid_query_longitude_too_big(builder):
    with pytest.raises(ValueError):
        builder.build_query(34, 500, "CD")


def test_invalid_query_bad_site_class(builder):
    with pytest.raises(ValueError):
        builder.build_query(34, -118, "X")
