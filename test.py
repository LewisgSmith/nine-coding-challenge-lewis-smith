import json
import requests
f = open('test.json', 'w')

requests.post('https://nine-coding-challenge-lsmith.herokuapp.com/', json=json.dump("new.csv", f))