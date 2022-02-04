import json
import yfinance

def extract_tickers(stocks):
  tickers = ''
  for stock in stocks:
    tickers = tickers + ' ' +stock['symbol']
  
  # Removing unwanted space at beginning on the symbols string
  return tickers.lstrip()

def main():
  # Opening JSON file
  stocks_file = open('data/yahoo_stocks.json')
 
  # returns JSON object as a dictionary
  yahoo_stocks = json.load(stocks_file)

  tickers = extract_tickers(yahoo_stocks)

  yf_tickers = yfinance.Tickers(tickers)

  prices = list()
  for ticker in yf_tickers.tickers:
    prices.append(yf_tickers.tickers[ticker].download(period="max"))

  print('debug')
  

if __name__ == '__main__':
  main()