import json
from logging.handlers import SYSLOG_UDP_PORT
import requests

returned_data = {}

def filter(data):
    j = 0
    for i in data['payload']:
        if i.get('drm') == True and i.get('episodeCount') > 0:
            j+=1
            testList = [str(i.get('image')), i.get('slug'), i.get('title')]
            testDict = dict.fromkeys(testList)
            #if i.get('drm') == True and i.get('episodeCount') > 0:
            returned_data[j] = testDict
    #print(json.dumps(data['payload']))
    testerList = ["response:", returned_data]
    print(json.dumps(testerList))
url = requests.get("https://mocki.io/v1/05bdf9aa-28f8-4e75-9698-29ccf8cbda3a", timeout=None)
output = json.loads(url.text)
print(filter(output))