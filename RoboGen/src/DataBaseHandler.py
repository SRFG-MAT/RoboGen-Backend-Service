import json

# -------------------------------------------------------------------------------------------
# store json myCalendar
# -------------------------------------------------------------------------------------------
def storeMyCalendar(entry):

    with open('database/calendar.json') as json_file:
        data = json.loads(json.load(json_file))
        temp = data['cal']
        temp.append(entry)
        new = '{"cal": ' + json.dumps(temp) + '}' 

    with open('database/calendar.json','w') as f:
        json.dump(new, f, indent=4)

# -------------------------------------------------------------------------------------------
# edit json myCalendar
# -------------------------------------------------------------------------------------------
def editMyCalendar(entry):

    with open('database/calendar.json') as json_file:
        data = json.loads(json.load(json_file))
        temp = data['cal']

        for item in temp:
            if item['title'] == entry['title']:
                item = entry

        new = '{"cal": ' + json.dumps(temp) + '}' 

    with open('database/calendar.json','w') as f:
        json.dump(new, f, indent=4)


# -------------------------------------------------------------------------------------------
# load json myCalendar
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
    "cal": []
    }"""

    with open('database/calendar.json','w') as f:
        json.dump(base, f, indent=4)
