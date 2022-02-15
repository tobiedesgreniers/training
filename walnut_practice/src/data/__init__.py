import os
import json
import pandas as pd


dirname = os.path.dirname(__file__)
data_path = os.path.join(dirname, 'data.json')

with open(data_path) as data_file:    
    recipes = json.load(data_file)['recipes']

#data = pd.json_normalize(data['recipes'])

def loadData():
    with open(data_path) as json_file:
        data = json.load(json_file)
    return data['recipes']

def saveData():
    with open(data_path, 'w') as json_file:
        json.dump({'recipes': [data]}, json_file, sort_keys=True, indent=4)
    return