class SeismicData_AASHTO2023:
    """
    Structure for ground motion data retrieved from USGS website
    """
    
    # json keys from query response
    __REQUEST_KEY = 'request'
    __RESPONSE_KEY = 'response'
    __METADATA_KEY = 'metadata'
    __DATA_KEY = 'data'

    def __init__(self, data: dict) -> None:
        self.__data = data

    def spectral_acceleration_as(self):
        """
        The design response spectrum acceleration coefficient at a period
        of zero seconds
        """
        return self.y_data[0]

    @property
    def latitude(self) -> float:
        """
        Latitude entered as part of the web query
        """
        return self.__data[self.__REQUEST_KEY]['latitude']
    
    @property
    def longitude(self) -> float:
        """
        Longitude entered as part of the web query
        """
        return self.__data[self.__REQUEST_KEY]['longitude']
    
    def sd1(self) -> float:
        """
        90 percent of the maximum value of the product, T*Sa, for periods
        from 1 to 2 seconds for sites with average shear wave velocity
        greater than 1,450 feet per second and for periods 1 to 5 seconds
        for sites with average shear wave velocity less than or equal to
        1,450 feet per second, but not less than 100 percent of the value of
        Sa at 1.0 second.

        Refer to AASHTO Guide Specifications for LRFD Seismic Bridge Design,
        3rd Edition - Section 3.5
        """
        # index values for range of data for sd1 calculation
        one_second_index = self.x_data.index(1.0)
        two_second_index = self.x_data.index(2.0)
        five_second_index = self.x_data.index(5.0)

        sd1_limit = self.y_data[one_second_index]

        ts_product = [self.x_data[i] * self.y_data[i] for i in range(len(self.x_data)) ]

        # Site classes A through C are defined as having average shear
        # wave velocities greater than 1,450 feet per second
        if self.site_class in ['A', 'B', 'BC', 'C']:
            sd1_product = 0.9 * max(ts_product[one_second_index:two_second_index + 1])
        else:
            sd1_product = 0.9 * max(ts_product[one_second_index:five_second_index + 1])

        return max(sd1_limit, sd1_product)
    
    def sds(self):
        """
        90 percent of the peak Sa value

        AASHTO Guide Specifications for LRFD Seismic Bridge Design,
        3rd Edition - Section 4.3.3
        """
        return 0.9 * max(self.y_data)
    
    def seismic_design_category(self) -> str:
        """
        Seismic design category as defined in Table 3.5-1 of the AASHTO
        Guide Specifications for LRFD Seismic Bridge Design, 3rd Edition
        """
        sd1 = self.sd1()
        if sd1 < 0.15:
            return 'A'
        elif 0.15 <= sd1 < 0.30:
            return 'B'
        elif 0.30 <= sd1 < 0.50:
            return 'C'
        else:
            return 'D'

    @property
    def site_class(self) -> str:
        """
        Site class returned in the output from AASHTO-2023 Web Services
        """
        return self.__data[self.__RESPONSE_KEY][self.__METADATA_KEY]['siteClass']
    
    @property
    def url(self) -> str:
        """
        URL query used to generate the output seismic data
        """
        return self.__data['url']
    
    @property
    def x_data(self) -> list:
        """
        x-coordinate values corresponding to the period in seconds
        """
        return self.__data[self.__RESPONSE_KEY][self.__DATA_KEY]['xs']
    
    @property
    def x_label(self) -> str:
        """
        x-axis graph label
        """
        return self.__data[self.__RESPONSE_KEY][self.__METADATA_KEY]['xLabel']
    
    @property
    def y_data(self) -> list:
        """
        y-coordinate values corresponding to the spectral acceleration as a ratio
        of the accelration due to gravity, g
        """
        return self.__data[self.__RESPONSE_KEY][self.__DATA_KEY]['ys']

    @property
    def y_label(self) -> str:
        """
        y-axis graph label
        """
        return self.__data[self.__RESPONSE_KEY][self.__METADATA_KEY]['yLabel']
