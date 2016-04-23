from app.modules.interfaces.Map import MapPoint
from app.modules.interfaces.Weather import OpenWeatherMap, WeatherMapClick


OPEN_WEATHER = "openwheather"
WEATHER_GOV = "wheathergov"

class WeatherFactory(object):
    """Factory to manager different wheather drivers
    """
    weather_sources = {WEATHER_GOV  : WeatherMapClick(),
                       OPEN_WEATHER : OpenWeatherMap()}

    @staticmethod
    def new_weather(service=OPEN_WEATHER):
        """Return a wheater object
        >>> factory = WeatherFactory.new_weather(OPEN_WEATHER)
        >>> factory.point = MapPoint("-31.000","-64.000")
        >>> factory.request()
        >>> print factory.answer()
        """
        weather_obj = WeatherFactory.weather_sources.get(service)
        return weather_obj



if __name__ == '__main__':
    factory = WeatherFactory.new_weather(OPEN_WEATHER)
    factory.point = MapPoint("-31.000","-64.000")
    factory.request()
    print factory.answer()
