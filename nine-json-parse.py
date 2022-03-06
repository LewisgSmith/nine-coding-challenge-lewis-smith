import json
import requests
f = open('test.json')

#requests.post('https://nine-coding-challenge-lsmith.herokuapp.com/', json=json.dump("new.csv", f))
url = requests.get("https://jsonplaceholder.typicode.com/todos/1")
output = json.loads(url.text)
print(output)

def filter():
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