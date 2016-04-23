from app.modules.factory.WeatherFactory import (WeatherFactory,
                                                OPEN_WEATHER,
                                                WEATHER_GOV)
from app.modules.interfaces.Map import MapPoint

class WeatherMng(object):
    """Manage conection with weather sources
    >>> weather = WeatherMng()
    >>> from app.modules.interfaces.Map import MapPoint
    >>> weather.point = MapPoint("-31.000","-64.000")
    >>> print weather.get_wheater()
    """
    def __init__(self, map_point=None):
        self.__point = map_point

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, map_point):
        self.__point = map_point

    def coordinates(self, latitude, longitude):
        self.point = MapPoint(latitude, longitude)

    def get_wheater(self):
        """:return: return a weather answer object
        :rtype: WeatherAnswer
        """
        factory = WeatherFactory.new_weather(OPEN_WEATHER)
        factory.point = self.__point
        factory.request()
        return factory.answer()


if __name__ == '__main__':
    tiempo = WeatherMng()
    tiempo.point = MapPoint("-31.000","-64.000")
    print tiempo.get_wheater()
