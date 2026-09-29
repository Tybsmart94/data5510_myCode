import requests
import json

DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

params = {
    "$where": "state='UT' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
    "$order": "end_date ASC"
}
req = requests.get(BASE_URL, params=params)
# print(req.text)
dict_full = json.loads(req.text)
# print(dict_full)

#Variables needed for getting the average
weekly_cases = 0
week_counter = 0

#Variables for getting the highest date
case_list = []
highest_date = ''
counter = 0

#Variables needed for getting the highest month
highest_month = 0
month_list = []

print(f"State Name: UT")

for i in dict_full:
    #Gets the total average
    num_cases = float(i["new_cases"])
    weekly_cases += num_cases
    week_counter += 1

    #Gets the highest date
    case_list.append(num_cases)
    if case_list[counter] == max(case_list):
        highest_date = i["end_date"]
    counter += 1

    #Get the highest month
    

avg_cases = weekly_cases/week_counter
print(f"The total number of weekly cases is {round(avg_cases, 2)}")
print(f"The date with the highest number of new Covid cases: {highest_date} ({max(case_list)})")
print(f"Month and Year, with the highest new number of covid cases: ")
print(f"Month and Year, with highest new number, percentage of population: {round(({highest_month}/3271616)*100, 2)} (3271616)")

