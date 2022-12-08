import pandas as pd
import requests
import lxml
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import undetected_chromedriver
import time
import collections
from collections import Counter


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
        if df3['Names'].loc[d] != 'Mirana':
            if df3['Names'].loc[d] != 'Silencer':
                if df3['Names'].loc[d] != 'Windranger':
                    if 'Spirit' not in df3['Names'].loc[d]:
                        carry.append((df3['Names'].loc[d]).replace('-', '_').replace(' ', '_'))
    d += 1
carry.pop(0)
# print(supports)
# print(carry)
d = 0
x = 0
svyazki = []
svyazki_win = []
for j in df1['team radiant 1p']:
    for name in carry:
        if j == name:
            p = df1.loc[d].tolist()
            del p[9:15]
            del p[0:4]

            cors = []
            for hero in p:
                for cor in carry:
                    if cor == hero:
                        cors.append(cor)

            sups = []
            for hero in p:
                for sup in supports:
                    if sup == hero:
                        sups.append(sup)

            for cs_ in cors:
                for sp in sups:
                    if cs_ == sp:
                        indx = cors.index(cs_)
                        cors.pop(indx)
            for c in cors:
                for s in sups:
                    svyazki.append(c + ' + ' + s)
                    if len(df1['winner'].loc[d]) > 13:
                        svyazki_win.append(c + ' + ' + s)
    d += 1

d = 0
for j in df1['team dire 1p']:
    for name in carry:
        if j == name:
            p = df1.loc[d].tolist()
            del p[0:9]

            cors = []
            for hero in p:
                for cor in carry:
                    if cor == hero:
                        cors.append(cor)

            sups = []
            for hero in p:
                for sup in supports:
                    if sup == hero:
                        sups.append(sup)

            for cs_ in cors:
                for sp in sups:
                    if cs_ == sp:
                        indx = cors.index(cs_)
                        cors.pop(indx)
            for c in cors:
                for s in sups:
                    svyazki.append(c + ' + ' + s)
                    if len(df1['winner'].loc[d]) < 13:
                        svyazki_win.append(c + ' + ' + s)
    d += 1














hm_sv_win = Counter(svyazki_win)
hm_sv = Counter(svyazki)
print(hm_sv)
print(hm_sv_win)
name_svyazki = []
kolvo_mathcey = []
wins = []
d = 0
for name_sv in hm_sv:
    if hm_sv[name_sv] > 20:
        name_svyazki.append(name_sv)
        kolvo_mathcey.append(round(((hm_sv[name_sv] * 100) / len(hm_sv)) * 10, 2))
    for hhh in hm_sv_win:
        if hm_sv[name_sv] > 20:
            if name_sv == hhh:
                wins.append(round((hm_sv_win[hhh] * 100) / hm_sv[name_sv], 2))
        d += 1
print(len(kolvo_mathcey))
print(len(wins))

df = pd.DataFrame({'carry + support': name_svyazki,
                   'pickrate': kolvo_mathcey,
                   'winrate': wins})
print(df)
df.to_excel('tabl_44444.xlsx')