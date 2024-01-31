from AASHTO2023Data.aashto_2023_config import Config_AASHTO2023
from AASHTO2023Data.query_format import QueryOutputFormat


class QueryBuilder_AASHTO2023:
    """
    Builds a web query string used to retrieve AASHTO 2023 Risk-Targeted
    Ground Motions from the USGS website (https://earthquake.usgs.gov/ws/designmaps/aashto-2023/)
    """
    def __init__(self, config: Config_AASHTO2023) -> None:
        self.__config: Config_AASHTO2023 = config

    def build_query(self, latitude: float, longitude: float, 
                    site_class: str, format: QueryOutputFormat = QueryOutputFormat.JSON) -> str:
        """
        Returns a query string for retrieving AASHTO 2023 Risk-Targeted Ground Motion
        data from the USGS website
        """
        JSON_FORMAT = "?format=JSON"
        CSV_FORMAT = "?format=CSV"

        if self.__latitude_outside_limits(latitude):
            raise ValueError('The latitude must be in the range {0} to {1}'.format(
                self.__config.latitude_min, self.__config.latitude_max
                ))
        
        if self.__longitude_outside_limits(longitude):
            raise ValueError('The longitude must be in the range {0} to {1}'.format(
                self.__config.longitude_min, self.__config.longitude_max
                ))
        
        if self.__site_class_not_valid(site_class):
            raise ValueError('The provided site class is not valid')

        query = self.__config.query_template.format(longitude, latitude, site_class)

        if format == QueryOutputFormat.CSV:
            return query + CSV_FORMAT
        else: # JSON is the default format
            return query + JSON_FORMAT
    
    def __latitude_outside_limits(self, latitude: float) -> bool:
        """
        Checks if the latitude is within the limits of the AASHTO 2023 Web Service
        """
        return float(latitude) < self.__config.latitude_min or float(latitude) > self.__config.latitude_max
    
    def __longitude_outside_limits(self, longitude: float) -> bool:
        """
        Checks if the longitude is within the limits of the AASHTO 2023 Web Service
        """
        return float(longitude) < self.__config.longitude_min or float(longitude) > self.__config.longitude_max
    
    def __site_class_not_valid(self, site_class: str):
        """
        Checks if site class value does not exist in the allowable site class list
        """
        return not site_class in self.__config.allowable_site_classes
