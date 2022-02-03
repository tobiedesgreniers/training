from bs4 import BeautifulSoup
import requests
import pandas as pd
import string
import json
from time import sleep

def get_json_listings(url):
  response = requests.get(url)
  if not response.ok:
    print(f'Code: {response.status_code}, url: {url}')
  return response.json()

def main():
  url = 'https://www.tsx.com/json/company-directory/search/tsx/'

  data = {}

  for letter in string.ascii_uppercase:
    print('Requesting company listings on TSX for letter ' + letter)
    data[letter] = get_json_listings(url+letter)
    print('Going to sleep for 5 seconds')
    sleep(5)
  
  data['0-9'] = get_json_listings(url+'0-9')

  with open('tsx_listings.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
  main()