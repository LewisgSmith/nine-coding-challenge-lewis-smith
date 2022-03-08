import json
import requests
import flask
from flask import request, Flask
returned_data = {}

app = Flask(__name__)

@app.route("/", methods=['POST'])

def filter(data):
    #j = 0
    responseList = []
    for i in data['payload']:
        if i.get('drm') == True and i.get('episodeCount') > 0:
            dict = {"image": i.get('image').get("showImage"), "slug": i.get('slug'), "title": i.get('title')}
            responseList.append(dict)
    returnDict = {"response": responseList}
    return json.dumps(returnDict, indent=4)

if request.method == 'POST':
    filter(json.loads(request.form))