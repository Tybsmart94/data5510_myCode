import requests
import json

#pulling data from a Web API
#Variables to query alphavantage
word = 'aggies'
search_word = 'usu'

key_word = "word"
key_score = "score"

# #Generate url
url = 'https://api.datamuse.com/words?ml=' + word
print(url)

request = requests.get(url)
# print(request.text)
dict_Full = json.loads(request.text)

#Programming Activity: Print word score for dunk
for i in dict_Full:
    if i["word"] == search_word:
        print(f"The score for the word {search_word} is: {i["score"]}")


