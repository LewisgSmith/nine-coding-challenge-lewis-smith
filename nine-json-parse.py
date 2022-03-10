import json
import requests
import flask
import gunicorn
from flask import request, Flask
returned_data = {}

app = Flask(__name__)
@app.route("/", methods=['POST', 'GET'])

def filter(data):
    #j = 0
    responseList = []
    for i in data['payload']:
        if i.get('drm') == True and i.get('episodeCount') > 0:
            dict = {"image": i.get('image').get("showImage"), "slug": i.get('slug'), "title": i.get('title')}
            responseList.append(dict)
    returnDict = {"response": responseList}
    return json.dumps(returnDict, indent=4)

def hello():
    if request.method == 'POST':
        try:
            request.form
            return filter(json.loads(request.form))
        except:
            return "<h1 style='color:red'>No request</h1>"   
    else:
        return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__name__":
    app.run(host='0.0.0.0')