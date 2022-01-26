import requests
import pandas as pd
import json
import os.path
from os import path

URL = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=655c9c39581929ef9632ef8beae948fb"

if not path.exists('data.json'):
  r = requests.get(URL)

  data = r.json()

  # Saving Data so we don't have to query the API each time
  with open('data.json', 'w') as f:
    json.dump(data, f)

  """ with open('data.json', 'w', encoding='utf-8') as f:
  json.dump(data, f, ensure_ascii=False, indent=4) """

f = open('data.json')
data = json.load(f)
f.close()

df = pd.DataFrame.from_dict(data['rates'], orient="index", columns=["Rates"])

df.to_csv('exchange_rates.csv')
