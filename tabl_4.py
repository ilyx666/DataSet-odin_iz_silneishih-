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

df1 = pd.read_excel(r'C:\Users\ilyx\Desktop\for py\tabl_3000_1.xlsx', index_col=0)
df3 = pd.read_excel(r'C:\Users\ilyx\Desktop\for py\333333.xlsx', index_col=0)


supports = []
carry = []
d = 0
for i in df3['roles']:
    if 'Support' in i:
        if df3['Names'].loc[d] != 'Alchemist':
            if df3['Names'].loc[d] != 'Kunkka':
                if df3['Names'].loc[d] != 'Naga Siren':
                    supports.append((df3['Names'].loc[d]).replace('-', '_').replace(' ', '_'))
    d += 1
d = 0
supports.pop(-1)
for i in df3['roles']:
    if 'Carry' in i:
        carry.append((df3['Names'].loc[d]).replace('-', '_').replace(' ', '_'))
    d += 1
carry.pop(0)
# print(supports)
# print(carry)
d = 0
x = 0
for j in df1['team radiant 1p']:
    for name in carry:
        if j == name:
            p = df1.loc[d].tolist()
            del p[9:15]
            del p[0:4]
            print(p)
            g = 0
            for sup in supports:
                if sup == p[g]:
                    print(sup)
    d += 1

