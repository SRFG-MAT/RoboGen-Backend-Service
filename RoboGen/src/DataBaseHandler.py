import json

# -------------------------------------------------------------------------------------------
# store json myCalender
# -------------------------------------------------------------------------------------------
def storeMyCalender(json):
	
	with open('database/calendar.json', 'w') as outfile:
		json.dump(data, outfile)
	
	# -------------------------------------------------------------------------------------------
# store json myCalender
# -------------------------------------------------------------------------------------------
def loadMyCalender():
    
	with open('data.txt') as json_file:
		data = json.load(json_file)
    
	return data