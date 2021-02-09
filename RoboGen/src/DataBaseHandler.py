import json
import os, json
from datetime import date

#####################################################
# Section: MyCalendar	
#####################################################

# store json myCalendar
def storeMyCalendar(entry):

    with open('database/calendar.json') as json_file:
        data = json.loads(json.load(json_file))
        temp = data['cal']
        temp.append(entry)
        new = '{"cal": ' + json.dumps(temp) + '}' 

    with open('database/calendar.json','w') as f:
        json.dump(new, f, indent=4)

		
# edit json myCalendar
def editMyCalendar(entry):

    with open('database/calendar.json') as json_file:
        data = json.loads(json.load(json_file))
        temp = data['cal']

        for n, item in enumerate(temp):
            if item['title'] == entry['title']:
                temp[n]['date'] = entry['date']
                temp[n]['time'] = entry['time']
                temp[n]['repeat'] = entry['repeat']
                temp[n]['reminder'] = entry['reminder']

        new = '{"cal": ' + json.dumps(temp) + '}' 

    with open('database/calendar.json','w') as f:
        json.dump(new, f, indent=4)


# load json myCalendar
def loadMyCalendar():

    with open('database/calendar.json') as json_file:
        data = json.load(json_file)
    return data


# reset json myCalendar
def resetMyCalendar():

    base = """{
    "cal": []
    }"""

    with open('database/calendar.json','w') as f:
        json.dump(base, f, indent=4)


#####################################################
# Section: Nutrition
#####################################################

# search the nutrition table for the food search term
def searchFoodArray(searchTerm):

    entries = []
    with open('/database/food.json', 'r') as dt_file:
        dt_data = json.load(dt_file)

        i = 0
        for entry in dt_data:

            if entry['Lebensmittel'].lower() == searchTerm:
                entries.append(entry['Lebensmittel'])
                print ("Gefunden: " + entry['Lebensmittel'])

            i = i + 1

    return entries


# create JSON calendar entry
def createCalendarEntry(food, amount):

    today = date.today()
    str = "[" + today.strftime("%d/%m/%Y") + "]: " + food + "(" + amount + ")" +"\n"

    file = open('/database/nutrition.txt', "a") # 'a' -> append for writing if exists
    file.write(str) 
    file.close() 


# store json myNutrition
def storeMyNutrition(food, amount):

	entries = searchFoodArray(food)
    if not entries:
        return 'error'
    else:
        createCalendarEntry(entries[0], amount)
        return 'OK, ich habe das Nahrungsmittel' + entries[0] + 'deinem Ernaehrungstagebuch mit dem heutigen Datum hinzugefuegt!'


# edit json myNutrition
#def editMyNutrition(entry):


# load json myNutrition
#def loadMyNutrition():


# reset json myNutrition
#def resetMyNutrition():



#####################################################
# Section: MySettings
#####################################################

# store json mySettings
def storeMySettings(settings):

    with open('database/settings.json','w') as f:
        json.dump(settings, f, indent=4)


# load json mySettings
def loadMySettings():

    with open('database/settings.json') as json_file:
        data = json.load(json_file)
    return data

