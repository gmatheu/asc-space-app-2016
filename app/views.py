from app.modules.WeatherMng import WeatherMng
from flask import render_template, request, jsonify
from app import app



class UnavailableRespose(Exception):
    # default error
    status_code = 503

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.route('/')
@app.route('/index')
def index():
    data = {'title': 'Hello World'}
    return render_template("index.html",
                           title='Home',
                           data=data)



@app.route("/api/weather", methods=['GET'])
def weather_info():
    """Get Weather information about location.
    """
    result = "{\"result\":\"invalid request\"}"
    if request.method == 'GET':
        lat = str(request.args.get('lat'))
        lon = str(request.args.get('lon'))
        tiempo = WeatherMng()
        tiempo.coordinates(lat, lon)
        #tiempo.point = MapPoint(lat,lon)
        result = tiempo.get_wheater().to_json()
    resp = app.make_response(result)
    resp.mimetype = "text/json"
    return result



@app.errorhandler(UnavailableRespose)
def handle_invalid_usage(error):
    """
    Response when an error ocurr
    """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response



#xml = 'foo'
#resp = app.make_response(xml)
#resp.mimetype = "text/xml"
#return resp
