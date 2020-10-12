import urllib.parse
import httpx
from geojson import Feature, Point, FeatureCollection
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/echo-args')
def echo_args():
    return request.args

def station_to_feature(station):
    return Feature(geometry=Point(tuple(station['coordinates'].values())), properties=station)


@app.route('/')
def index():
    '''
    Take the GET args as arguments for OpenAQ Locations API arguments
    and convert the result to GeoJSON format
    '''
    args = urllib.parse.urlencode(request.args)
    openaq_url = f"https://api.openaq.org/v1/locations?{args}"
    response = httpx.get(openaq_url)
    stations = response.json()['results']
    collection = FeatureCollection([station_to_feature(station) for station in stations])
    return collection
