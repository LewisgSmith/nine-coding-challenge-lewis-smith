import json
from operator import truediv
f = open('test.json')
data = json.load(f)

response = {"error": "Could not decode request: JSON parsing failed"}

for i in data['payload']:
        if i.get('drm') == True and i.get('episodeCount') > 0:
            print i.get('drm')
            print i.get('episodeCount')