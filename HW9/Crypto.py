## Get info from https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin&vs_currencies=eth,btc
## You will lose points if you don't pull Cardano, use Try and Except to handle when Cardano isn't there
## "Cardano will have edges coming from it, but no edges going to it"

import networkx
import json
import time
from requests import get, post

counter = 0
##ids_list = ["ripple", "cardano", "bitcoin-cash", "eos", "litecoin", "ethereum", "bitcoin"]
##currencies_list = ["xrp", "ada", "bch", "eos", "ltc", "eth", "btc"]
#Shorter lists for testing so I don't hit rate limit
ids_list = ["ethereum", "bitcoin"]
currencies_list = ["eth", "btc"]
url_list = []

for i in ids_list:
    url_list.append(f"https://api.coingecko.com/api/v3/simple/price?ids={i},{ids_list[counter+1]}&vs_currencies={currencies_list[counter]},{currencies_list[counter+1]}")
    counter += 1
    if i == "ethereum":
        break

for url in url_list:
    try:
        results = get(url)
        json_results = results.json()
        print(json_results)
    except:
        print("No values to get")