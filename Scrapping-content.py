import pandas as pd
from bs4 import BeautifulSoup
import requests
from pprint import pprint as p
url = 'http://arena.siesgst.ac.in/contest/GSL02/status'

res = requests.get(url=url)
soup = BeautifulSoup(res.content, "html.parser")
# res = res.text
# p(res)
results = soup.find_all('div', class_='d-flex justify-content-center')
# print(results, "\n\n")

res = str(results).count("<a ")
print(res)


def table_data(soup):
    global df
    for t in soup.find_all('tr'):
        try:
            username = t.find_all('td')[2].text
            problem = t.find_all('td')[3].text
            verdict = t.find_all('td')[4].text
            language = t.find_all('td')[5].text
            time = t.find_all('td')[6].text
            memory = t.find_all('td')[7].text
            print(username, problem, verdict, language, time, memory)
            df = df.append({'username': username, 'problem': problem, 'verdict': verdict,
                           'language': language, 'time': time, 'memory': memory}, ignore_index=True)

        except:
            pass


df = pd.DataFrame(columns=['username', 'problem',
                  'verdict', 'language', 'time', 'memory'])


for i in range(res):
    url = 'http://arena.siesgst.ac.in/contest/GSL02/status?page=' + str(i)
    res = requests.get(url=url)
    soup = BeautifulSoup(res.content, "html.parser")
    table_data(soup)
df.to_csv('GSL02.csv', index=False)
