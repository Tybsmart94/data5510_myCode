import requests
import json

key = "12404453"
url = "https://api.discogs.com/releases/" + key

key_1 = 'title'
key_2 = 'duration'

req = requests.get(url)
dict_full = json.loads(req.text)

for i in dict_full["tracklist"]:
    print(i[key_1], ":", i[key_2])

