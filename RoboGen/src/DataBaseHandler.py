import json

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

