from enum import Enum


class QueryOutputFormat(Enum):
    """
    Available output formats for the USGS AASHTO 2023 Risk-Targeted
    Ground Motion Data
    """
    JSON = 0
    CSV = 1