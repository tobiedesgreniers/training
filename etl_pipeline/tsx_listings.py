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
  # For any manual verification, use the following URL
  # https://www.tsx.com/listings/listing-with-us/listed-company-directory
  url = 'https://www.tsx.com/json/company-directory/search/tsx/'

  data = {}

  # Generating list of possible index for stock URL
  letters = list(string.ascii_uppercase)
  letters.append('0-9')

  # Getting all stocks (from A to Z) from the TSX
  for letter in letters:
    print('Requesting company listings on TSX for letter ' + letter)
    data[letter] = get_json_listings(url+letter)
    print('Going to sleep for 5 seconds')
    sleep(5)

  # Saving data to JSON file
  with open('data/tsx_listings.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
  main()