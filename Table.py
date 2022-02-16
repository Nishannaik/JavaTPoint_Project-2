#import pandas as pd

#df = pd.read_html('https://www.javatpoint.com/splunk-types-of-command', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'})

#print(df)

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.javatpoint.com/python-history'
requests.get(url)
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
print(soup)

table_data = soup.find('table', class_ = 'alt')

headers = []
for i in table_data.find_all('th'):
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns = headers)

for j in table_data.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [tr.text for tr in row_data]
        length = len(df)
        df.loc[length] = row
        
        df.to_csv('Tables.csv')