# pegelonline-geojson
API-Wrapper for pegelonline api to provide geojson with Flask.
The [documentation](https://www.pegelonline.wsv.de/webservice/dokuRestapi) at pegelonline is still valid. Only change the base url.
To run the wrapper

    $ export FLASK_APP=hello.py
    $ flask run

## Example
The original API:

    $ curl -X GET https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/K%C3%96LN.json
    {
    	"uuid": "a6ee8177-107b-47dd-bcfd-30960ccc6e9c",
    	"number": "2730010",
    	"shortname": "Köln",
    	"longname": "KÖLN",
    	"km": 688.0,
    	"agency": "WSA DUISBURG-RHEIN",
    	"longitude": 6.963300159749653,
    	"latitude": 50.93694925646438,
    	"water": {
      		"shortname": "RHEIN",
      		"longname": "RHEIN"
    	}
    }

The wrapper API:

    $ curl -X GET http://127.0.0.1:5000/stations/K%C3%96LN.json
    {"geometry": {"coordinates": [50.93694925646438, 6.963300159749653], "type": "Point"}, "type": "Feature", "properties": {"shortname": "K\u00f6ln", "km": 688.0, "uuid": "a6ee8177-107b-47dd-bcfd-30960ccc6e9c", "agency": "WSA DUISBURG-RHEIN", "longname": "K\u00d6LN", "number": "2730010", "water": {"longname": "RHEIN", "shortname": "RHEIN"}}}


## Live Demo
For a live demo you can use http://tools.bengs.cologne/pegelonline/
