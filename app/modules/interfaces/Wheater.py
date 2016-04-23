import requests
import json
from app.modules.interfaces.Map import MapPoint

#class Wheather
#http://forecast.weather.gov/MapClick.php?lat=60.906&lon=-162.4406&unit=0&lg=english&FcstType=kml&FcstType=kml&KmlType=Forecast
#import urllib2


#def homepage(request):
#    file = urllib2.urlopen('https://www.goodreads.com/review/list/20990068.xml?key=nGvCqaQ6tn9w4HNpW8kquw&v=2&shelf=toread')
#    data = file.read()
#    file.close()
#    dom = parseString(data)
#http://forecast.weather.gov/MapClick.php?lat=60.906&lon=-162.4406&unit=0&lg=english&FcstType=json
#http://forecast.weather.gov/MapClick.php?lat=60.906&lon=60.906&unit=0&lg=english&FcstType=json




class WheatherBase(object):
    def __init__(self,map_point=None):
        self._base_url = "http://forecast.weather.gov/MapClick.php"
        self._format = "json"
        self._lang = "english"
        self._unit = "metric"
        self._point = map_point
        self._anwser = None

    @property
    def point(self, map_point):
        self._point = map_point

    @point.setter
    def point(self, map_point):
        self._point = map_point

    def _request(self):
        self._request_result = requests.get(self._build_url()).content
        print self._request_result
        self._build_answer()

    def _build_answer(self):
        self._anwser = json.loads(self._request_result)

    def answer(self):
        return self._anwser


class WheatherAnswer(object):
    self.temp = None



class WheatherMapClick(WheatherBase):
    def __init__(self, map_point=None):
        super(WheatherMapClick, self).__init__(map_point)
        self._request()


    def _build_url(self):
        url = "{base}?lat={lat}&lon={lon}&unit={unit}&lg=" \
                "{lang}&FcstType={type}".format(base=self._base_url,
                                                lat=self._point.latitude,
                                                lon=self._point.longitude,
                                                unit=self._unit,
                                                lang=self._lang,
                                                type=self._format)
        return url



class OpenWheatherMap(WheatherBase):
    """
    Open Wheather Map
    http://api.openweathermap.org/data/2.5/weather?lat=-31&lon=-64&appid=efee9eed3260befbe28588d89dfa620c
    """
    def __init__(self, map_point=None):
        super(OpenWheatherMap, self).__init__(map_point)
        self._apikey = "efee9eed3260befbe28588d89dfa620c"
        self._base_url = "http://api.openweathermap.org/data/2.5/weather"
        self._url_template = ("{base}?lat={lat}&lon={lon}"
                              "&units={unit}&appid={appid}")
        self._request()

    def _build_url(self):
        url = self._url_template.format(base=self._base_url,
                                    lat=self._point.latitude,
                                    lon=self._point.longitude,
                                    unit=self._unit,
                                    appid=self._apikey)
        return url



if __name__ == "__main__":
    #initial_point = MapPoint("60.906","-162.4406")
    initial_point = MapPoint("-31.000","-64.000")
    clima = OpenWheatherMap(initial_point)
    print clima.answer()


#{u'clouds': {u'all': 0}, u'name': u'Colonia Caroya', u'coord':
#{u'lat': -31.02, u'lon': -64.07}, u'sys':
#{u'country': u'AR', u'sunset': 1461447967,
#u'message': 0.0082, u'type': 3, u'id': 4688, u'sunrise': 1461408133},
#u'weather': [{u'main': u'Clear', u'id': 800, u'icon': u'01d',u'description': u'clear sky'}],
#u'cod': 200, u'base': u'cmc stations', u'dt': 1461423600, u'main':
#{u'pressure': 1007, u'temp_min': 296.15,
# u'temp_max': 296.15, u'temp': 296.15, u'humidity': 56},
#u'id': 3860801, u'wind': {u'speed': 2.1, u'deg': 50}}
