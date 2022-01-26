from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

html_data = requests.get(URL)
data = html_data.text

print(data[101:124])

soup = BeautifulSoup(html_data.content, 'html.parser')

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

# tr tags from thead are also found by find_all('tr')
# added [1:] to remove the first tr from the resultSet
for row in soup.find_all('tbody')[3].find_all('tr')[1:]:
    col = row.find_all('td')

    # List Comprehension
    values = [val.text.strip() for val in col]

    data.loc[len(data)] = values[1:3]

print(data.head(5))

data_json = data.to_json()
print(data_json)

