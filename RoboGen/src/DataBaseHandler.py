import json

# -------------------------------------------------------------------------------------------
# store json myCalendar
# -------------------------------------------------------------------------------------------
def storeMyCalendar(entry):

    with open('database/calendar.json') as json_file:
        data = json.load(json_file)
        temp = data['cal']
        data.append(entry)

    with open('database/calendar.json','w') as f:
        json.dump(data, f, indent=4)

# -------------------------------------------------------------------------------------------
# store json myCalendar
# -------------------------------------------------------------------------------------------
def loadMyCalendar():

    with open('database/calendar.json') as json_file:
        data = json.load(json_file)
    return data

# -------------------------------------------------------------------------------------------
# reset json myCalendar
# -------------------------------------------------------------------------------------------
def resetMyCalendar():

    base = """{
    "cal": [{
                "date": "2020-09-29",
                "reminder": "10",
                "repeat": 1,
                "time": "05:55",
                "title": "Beispiel"
		}],
    "calSettings": []
    }"""

    with open('database/calendar.json','w') as f:
        json.dump(base, f, indent=4)
