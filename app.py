from flask import Flask, request, render_template, redirect
from convert import to_feature, to_collection
import geojson
import json
import requests

API_URL = 'https://www.pegelonline.wsv.de/webservices/rest-api/v2'
app = Flask(__name__)


@app.route('/stations/<path>.json')
def station(path):
    '''
    Request to a selected gauge converts to a Feature
    '''
    req = requests.get(API_URL+request.path, params=request.args)
    station = json.loads(req.text)
    res = to_feature(station)
    response = app.response_class(
            response=geojson.dumps(res),
            status=200,
            mimetype='application/json')
    return response


@app.route('/stations.json')
def stations():
    '''
    Request to more than one gauge converts to FeatureCollection
    '''
    req = requests.get(API_URL+request.path, params=request.args)
    stations = json.loads(req.text)
    res = to_collection(stations)
    response = app.response_class(
            response=geojson.dumps(res),
            status=200,
            mimetype='application/json')
    return response


@app.route('/')
def index():
    '''
    Custom index page
    '''
    return render_template('index.html')


@app.route('/<path:path>')
def redirect_pegelonline(path):
    '''
    Redirect all api requests without location information
    '''
    return redirect(API_URL+'/'+path)
