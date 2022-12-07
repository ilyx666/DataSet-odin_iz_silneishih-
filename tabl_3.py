import pandas as pd
import requests
import lxml
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import undetected_chromedriver
import time
import collections


pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)


request_site = Request(url='https://liquipedia.net/dota2/Hero_statistics', headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"})
webpage = urlopen(request_site)
soup__ = BeautifulSoup(webpage, 'lxml')
for_names = soup__.find_all('td', class_='smwtype_wpg')
for_dmg = soup__.find_all('td', class_='Base-Dmg smwtype_num')
for_armr = soup__.find_all('td', class_='Base-Armor smwtype_num')
for_ms = soup__.find_all('td', class_='Base-Move-Speed smwtype_num')
for_at = soup__.find_all('td', class_='Attack-Type smwtype_txt')


names = []
dmg = []
armor = []
ms = []
at = []


for i in for_names:
    names.append(i.text)

for damage in for_dmg:
    dmg.append(damage.text)

for amr in for_armr:
    armor.append(amr.text)

for mss in for_ms:
    ms.append(mss.text)

for att in for_at:
    at.append(att.text)


request_site = Request(url='https://dota2.ru/heroes/', headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"})
webpage = urlopen(request_site)
soup__ = BeautifulSoup(webpage, 'lxml')
for_roles = soup__.find_all('a')


roles = {}
d = 0
for j in for_roles:
    if 257 > d > 132:
        if d != 157:
            role = str(j.get('data-role')).replace('-', '_')
            name = str(j.get('data-tooltipe'))
            roles[name] = role
    d += 1


role_na_ruke = []
for v in sorted(roles):
    role_na_ruke.append(roles[v])


df = pd.DataFrame({'Names': names,
                   'Base dmg': dmg,
                   'Base armor': armor,
                   'Base ms': ms,
                   'Attack type': at,
                   'roles': role_na_ruke})
print(df)
df.to_excel('333333.xlsx')