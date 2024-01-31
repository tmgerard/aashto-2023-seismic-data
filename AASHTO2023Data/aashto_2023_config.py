import json


class Config_AASHTO2023:
    """
    Loads configuration JSON file and provides access to the configuration
    variables applicable to the AASHTO 2023 Risk-Targeted Ground Motion
    Data from USGS.
    """
    __CONFIG_STR = 'aashto-2023'

    def __init__(self, config_file_path: str) -> None:
        self.__config_file_path = config_file_path
        self.__load_config()
    
    def __load_config(self) -> None:
        """
        Loads the seismic configuration JSON file
        """
        with open(self.__config_file_path, 'r', encoding='utf-8') as file:
            self.__config = json.load(file)
    
    @property
    def query_template(self) -> str:
        """
        Template string for the AASHTO 2023 USGS web query
        """
        return self.__config[self.__CONFIG_STR]['query']
    
    @property
    def latitude_max(self) -> float:
        """
        Maximum allowable latitude that can be used in the query
        """
        return float(self.__config[self.__CONFIG_STR]['latitude-max'])
    
    @property
    def latitude_min(self) -> float:
        """
        Minimum allowable latitude that can be used in the query
        """
        return float(self.__config[self.__CONFIG_STR]['latitude-min'])
    
    @property
    def longitude_max(self) -> float:
        """
        Maximum allowable longitude that can be used in the query
        """
        return float(self.__config[self.__CONFIG_STR]['longitude-max'])
    
    @property
    def longitude_min(self) -> float:
        """
        Minimum allowable longitude that can be used in the query
        """
        return float(self.__config[self.__CONFIG_STR]['longitude-min'])
    
    @property
    def allowable_site_classes(self) -> list:
        """
        List of allowable site classes that can be used in the query
        """
        return self.__config[self.__CONFIG_STR]['allowable-site-classes']
