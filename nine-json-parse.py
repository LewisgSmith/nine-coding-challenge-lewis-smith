import json
import requests
f = open('test.json')

def filter(data):
    #data = json.load(f) - loading from the file
    responseList = []
    #initialising list variable
    for i in data['payload']:
         #for the data
        if i.get('drm') == True and i.get('episodeCount') > 0:
            #Checks that the given criteria are both true
            entry = [i.get('image'), i.get('slug'), i.get('title')]
            #sets the entry as a list - change this to dict for JSON
            responseList.append(entry)
            #adds the entry to the list of correct data
            response = json.dumps(responseList)
            # Change dumps to dump, as that will allow for output to JSON
            print(response)
            
#requests.post('https://nine-coding-challenge-lsmith.herokuapp.com/', json=json.dump("new.csv", f))
url = requests.get("https://mocki.io/v1/39cd8b16-b3fc-4929-a0b2-fd3565d7f08d")
output = json.loads(url.text)
filter(output)