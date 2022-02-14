import json

data = {}

def loadData():
    with open("data.json") as json_file:
        data = json.load(json_file)
    return data

def saveData():
    with open("data.json", 'w') as json_file:
        json.dump(data, json_file, sort_keys=True, indent=4)
    return