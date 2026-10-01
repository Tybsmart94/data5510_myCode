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

#Makes URL
DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

#Variables used in all to iterate through the states_pop list
state_counter = -2

#Variables to store all 50 state values for final summary
highest_state = '' #So we can print the states out in the final summary
lowest_state = ''
saddeset_date = '' #So we can print the dates out in the final summary
happiest_date = ''
highest_cases = '' #So we can print the cases out in the final summary
lowest_cases = ''
best_population = '' #So we can print the population out in the final summary
worst_population = ''
state_percentages = []


for state in states_list:
    #Dictionary to dump into a json file
    state_dict = {"state_name" : '', "state_pop" : 0, "avg_cases" : 0, "highest_date" : '', "highest_cases" : 0, "highest_month" : '', "month_cases" : 0, "percentage" : 0}
    #Iterates through state_pop list for when that gets set up
    state_counter += 2  
    if state_counter == 100:
        print("==================== SUMMARY ACROSS ALL STATES ====================")
        print("State with HIGHEST percentage of population during its highest month:")
        print(f"{highest_state} - {max(state_percentages)} in {saddeset_date} ({highest_cases} cases; Population: {best_population})")
        print()
        print("State with LOWEST percentage of population during its highest month:")
        print(f"{lowest_state} - {min(state_percentages)} in {happiest_date} ({lowest_cases} cases; Population: {worst_population})")
        break

    curr_state = states_list[state_counter]
    print(f"State Name: {curr_state}")
    params = {
    "$where": f"state='{curr_state}' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
    "$order": "end_date ASC"
    }
    req = requests.get(BASE_URL, params=params)
    dict_full = json.loads(req.text)

    #Variables needed for getting the average
    weekly_cases = 0
    week_counter = 0

    #Variables for getting the highest date
    case_list = []
    highest_date = ''
    counter = 0

    #Variables needed for getting the highest month
    month_list = []
    month_case_list = []

    for i in dict_full:
        state = i["state"]
        if state == curr_state:
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
            month_cases = float(i["new_cases"])
            month_case_list.append(month_cases)

    #More variables I will need to get the highest month
    total_month_list = []
    current_month = [0][0:7]
    total_month = 0
    highest_month = ''
    counter2 = 0

    for i in range(len(month_list)):
        month = month_list[i][0:7]
        
        if month == current_month:
            total_month += month_case_list[i]
        else:
            total_month_list.append(total_month)
            if total_month == max(total_month_list):
                highest_month = month

            current_month = month
            total_month = month_case_list[i]
            counter2 += 1
        

    total_month_list.append(total_month) 

    #Finalizes average and percentage
    avg_cases = weekly_cases/week_counter
    percentage = round(max(total_month_list)/states_list[state_counter+1] * 100, 2)

    #Checks stuff for the final summary
    state_percentages.append(percentage)
    if percentage == max(state_percentages):
        highest_state = curr_state
        saddeset_date = highest_month
        highest_cases = max(total_month_list)
        best_population = states_list[state_counter+1]
    if percentage == min(state_percentages):
        lowest_state = curr_state
        happiest_date = highest_month
        lowest_cases = max(total_month_list)
        worst_population = states_list[state_counter+1]

    #Final output
    print(f"The average number of weekly cases is {round(avg_cases, 2)}")
    print(f"The date with the highest number of new Covid cases: {highest_date} ({max(case_list)})")
    print(f"Month and Year, with the highest new number of covid cases: {highest_month} ({max(total_month_list)})")
    print(f"Month and Year, with highest new number, percentage of population: {percentage} ({states_list[state_counter+1]})")
    print("------------------------------------------------------------")

    #Updates dictionary
    state_dict["state_name"] = curr_state
    state_dict["state_pop"] = states_list[state_counter+1]
    state_dict["avg_cases"] = round(avg_cases, 2)
    state_dict["highest_date"] = highest_date
    state_dict["highest_cases"] = max(case_list)
    state_dict["highest_month"] = highest_month
    state_dict["month_cases"] = max(total_month_list)
    state_dict["percentage"] = percentage

    #dumps values into a json file
    json.dump(state_dict, open(f"/home/ubuntu/data5510_myCode/HW5/data/{curr_state}.json", "w"), indent = 4)