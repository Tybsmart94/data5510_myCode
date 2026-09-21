import requests
import json

#Dictionaries
dict = {
    "employees": [
        {"firstName": "John", "lastName": "Doe"},
        {"firstName": "Anna", "lastName": "Smith"},
        {"firstName": "Peter", "lastName": "Jones"},
    ]
}

#How to iterate through a dictionary, that has a list of dictionaries in it
for i in dict["employees"]:
    print(i["firstName"])

#pulling data from a Web API
#Variables to query alphavantage
word = "duck"

# #Generate url
url = "https://api.datamuse.com/words?ml=" + word
print(url)

request = requests.get(url)
print(request.text)
dict_Full = json.loads(request.text)

#Programming Activity: Print word score for dunk
for i in dict_Full:
    if i["word"] == "dunk":
        print(i["score"])




