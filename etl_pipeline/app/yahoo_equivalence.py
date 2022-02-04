import json
import string

def extract_stocks(listings):
  letters = list(string.ascii_uppercase)
  letters.append('0-9')
  results = list()

  for letter in letters:
    # Used nested list comprehension at first, but it was too hard to obtain the granularity we want for processing tradable instruments
    for listing in listings[letter]['results']:
      if (validate_stock(listing) and validate_stock(listing['instruments'][0])):
        # Listings may appear in multiple JSON documents from the TSX
        # Check for uniqueness
        if(listing['instruments'][0] not in results):
          results.append(listing['instruments'][0])

  return results


def validate_stock(tradable):
  return (validate_symbol(tradable['symbol']) and validate_name(tradable['name']))


def validate_symbol(symbol):
  if('.' in symbol):
    code = symbol.split('.')
  
    validation = code[1] not in ('UN', 'DB', 'WT', 'U', 'V', 'PR', 'PF', 'X')
    return validation
  
  return True

def validate_name(name):
  lower_name = name.lower()
  validation = (
    'fund'  not in lower_name and
    'etf'   not in lower_name and
    'trust' not in lower_name and
    'bond'  not in lower_name and
    'split' not in lower_name and
    'reit'  not in lower_name
  )

  return validation


def convert_to_yahoo(stocks):
  for i in range(len(stocks)):
    if '.' in stocks[i]['symbol']:
      stocks[i]['symbol'] = stocks[i]['symbol'].replace('.','-')
    stocks[i]['symbol'] = stocks[i]['symbol'] + '.TO'
  
  return stocks
  


def main():
  # Opening JSON file
  listings_file = open('data/tsx_listings.json')
 
  # returns JSON object as a dictionary
  tsx_listings = json.load(listings_file)

  stocks = extract_stocks(tsx_listings)

  with open('data/filter_stock.json', 'w', encoding='utf-8') as file:
    json.dump(stocks, file, ensure_ascii=False, indent=4)

  yahoo_stocks = convert_to_yahoo(stocks)

  with open('data/yahoo_stocks.json', 'w', encoding='utf-8') as file:
    json.dump(yahoo_stocks, file, ensure_ascii=False, indent=4)



if __name__ == '__main__':
  main()