import json
from logging.handlers import SYSLOG_UDP_PORT
import requests

returned_data = {}

def filter(data):
    #j = 0
    responseList = []
    for i in data['payload']:
        if i.get('drm') == True and i.get('episodeCount') > 0:
            dict = {"image": i.get('image').get("showImage"), "slug": i.get('slug'), "title": i.get('title')}
            responseList.append(dict)
    returnDict = {"response": responseList}
    return json.dumps(returnDict, indent=4)


url = requests.get("https://mocki.io/v1/05bdf9aa-28f8-4e75-9698-29ccf8cbda3a", timeout=None)
output = json.loads(url.text)
print(filter(output))