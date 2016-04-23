__author__ = "jcortes, frodriguez"

import requests
import json
from app.modules.interfaces.Map import MapPoint

"""
Weather interface with forecast.weather.gov and api.openweathermap.org.
Query examples:
Weather:
http://forecast.weather.gov/MapClick.p
hp?lat=60.906&lon=-162.4406&unit=0&lg=english&FcstType=json
Open weather:
http://api.openweathermap.org/data/2.5/weather?lat=-31&lon=-64
&appid=efee9eed3260befbe28588d89dfa620c
"""


class WeatherAnswer(object):
    def __init__(self, source, **args):
        """ This class filters the args passed with
        relevant keys for forward-to-view.
        :param source: The weather source
        :param args: The json response from source
        """

        keys = ('temp', 'temp_min', 'temp_max', 'humidity',
                'pressure', 'wind_speed', 'dt')
        self.args = {k: args.get(k, None) for k in keys}
        self.args['source'] = source

    def set_key(self, key, value):
        self.args[key] = value

    def to_json(self):
        return json.dumps({'weather': self.args,
                           'msg': '',
                           'success': True})


class WeatherBase(object):
    def __init__(self, map_point=None):
        self._format = None
        self._lang = None
        self._unit = None
        self._point = map_point
        self._anwser = None
        self._source = None

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, map_point):
        self._point = map_point

    def _build_url(self):
        # Virtual method.
        pass

    def request(self):
        self._request_result = requests.get(self._build_url()).content
        self._build_answer()

    def _build_answer(self):
        pass

    def answer(self):
        return self._anwser


class WeatherMapClick(WeatherBase):
    """ Weather.gov map.
    Endpoint: http://forecast.weather.gov/MapClick.php
    """

    _base_url = "http://forecast.weather.gov/MapClick.php"

    def __init__(self, map_point=None):
        super(WeatherMapClick, self).__init__(map_point)
        self._format = "json"
        self._lang = "english"
        self._unit = "metric"
        self._source = "WPC"

    def _build_url(self):
        url = ("{base}?lat={lat}&lon={lon}&unit={unit}&lg="
               "{lang}&FcstType={type}").format(base=self._base_url,
                                                lat=self._point.latitude,
                                                lon=self._point.longitude,
                                                unit=self._unit,
                                                lang=self._lang,
                                                type=self._format)
        return url

    def _build_answer(self):
        answer = json.loads(self._request_result)
        temperature = (answer.get('data', {}).get('temperature'))
        current = answer.get('currentobservation')

        self._anwser = WeatherAnswer(source=self._source,
                                     temp=temperature[0],
                                     temp_min=None,
                                     temp_max=None,
                                     humidity=None,
                                     pressure=None,
                                     wind_speed=current.get('Winds'),
                                     dt=current.get('Date'))


class OpenWeatherMap(WeatherBase):
    """ Open Weather Map.
    Endpoint: http://api.openweathermap.org/data/2.5/weather
    Usage:
    >>> initial_point = MapPoint("-31.000", "-64.000")
    >>> clima = OpenWeatherMap(initial_point)
    >>> clima.request()
    >>> clima.answer()
    """

    _base_url = "http://api.openweathermap.org/data/2.5/weather"

    def __init__(self, map_point=None):
        super(OpenWeatherMap, self).__init__(map_point)
        self._apikey = "efee9eed3260befbe28588d89dfa620c"
        self._url_template = ("{base}?lat={lat}&lon={lon}"
                              "&units={unit}&appid={appid}")
        self._unit = "metric"
        self._source = "OWM"

    def _build_url(self):
        url = self._url_template.format(base=self._base_url,
                                        lat=self._point.latitude,
                                        lon=self._point.longitude,
                                        unit=self._unit,
                                        appid=self._apikey)
        return url

    def _build_answer(self):
        answer = json.loads(self._request_result)
        main = answer.get('main')
        wind = answer.get('wind')
        self._anwser = WeatherAnswer(source=self._source,
                                     temp=main.get('temp'),
                                     temp_min=main.get('temp_min'),
                                     temp_max=main.get('temp_max'),
                                     humidity=main.get('humidity'),
                                     pressure=main.get('pressure'),
                                     wind_speed=wind.get('speed'),
                                     dt=answer.get('dt'))
