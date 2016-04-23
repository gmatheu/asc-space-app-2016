class MapPoint(object):
    """
    Point on map (latitude, longitude)
    """
    def __init__(self, lat=0, lon=0):
        self.__latitude = lat
        self.__longitude = lon

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, lat):
        self.__latitude = lat

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, lon):
        self.__longitude = lon
