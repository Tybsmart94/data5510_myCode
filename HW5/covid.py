#Imports
import requests
import json
import datetime

#Gets the population file into this python file and cleaned
states_file = open("/home/ubuntu/data5510_myCode/HW5/states.csv")
states_pop = states_file.readlines()
states_list = []

#Cleans the data
for lines in states_pop:
    lines = lines.rstrip("\n")
    lines = lines.split(",")
    lines[1] = int(lines[1])
    # print(lines)
    states_list.append(lines[0])
    states_list.append(lines[1])

# print(states_list)

#Gets URL and sets up parameters to keep it to just Utah stats
DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

params = {
    "$where": "state='UT' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
    "$order": "end_date ASC"
}
req = requests.get(BASE_URL, params=params)
# print(req.text)
dict_full = json.loads(req.text)
print(dict_full)

#Variables used in all to iterate through the states_pop list
state_counter = 0
tester = states_list[86]
tester2 = states_list[87] #This and line 37 are just for getting the UT part to work

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
month_case_list = []

print(f"State Name: {tester}")#{states_list[state_counter]}")

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
    months = i["start_date"]
    month_list.append(months)
    month_cases = i["new_cases"]
    month_case_list.append(month_cases)
    
print(month_list)
print(month_case_list)

#Iterates through state_pop list for when that gets set up
state_counter += 1    

#Finalizes average
avg_cases = weekly_cases/week_counter

#Final output
print(f"The average number of weekly cases is {round(avg_cases, 2)}")
print(f"The date with the highest number of new Covid cases: {highest_date} ({max(case_list)})")
print(f"Month and Year, with the highest new number of covid cases: ({max(month_list)})")
print(f"Month and Year, with highest new number, percentage of population: {round((228454/tester2) * 100, 2)} ({tester2})")