import pandas as pd
from collections import Counter
import math


pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)


df = pd.read_excel(r'C:\Users\ilyx\Desktop\for py\tabl_3000_1.xlsx', index_col= 0 )

all_heroes = []


d = 0
for i in df['team radiant 1p']:
    all_heroes.append(i)
for i in df['team radiant 2p']:
    all_heroes.append(i)
for i in df['team radiant 3p']:
    all_heroes.append(i)
for i in df['team radiant 4p']:
    all_heroes.append(i)
for i in df['team radiant 5p']:
    all_heroes.append(i)
for i in df['team dire 1p']:
    all_heroes.append(i)
for i in df['team dire 2p']:
    all_heroes.append(i)
for i in df['team dire 3p']:
    all_heroes.append(i)
for i in df['team dire 4p']:
    all_heroes.append(i)
for i in df['team dire 5p']:
    all_heroes.append(i)


d = 0
hero_winners = []
for i in df['winner']:
    if len(i) > 13:
        hero_winners.append(df['team radiant 1p'].loc[d])
        hero_winners.append(df['team radiant 2p'].loc[d])
        hero_winners.append(df['team radiant 3p'].loc[d])
        hero_winners.append(df['team radiant 4p'].loc[d])
        hero_winners.append(df['team radiant 5p'].loc[d])
    else:
        hero_winners.append(df['team dire 1p'].loc[d])
        hero_winners.append(df['team dire 2p'].loc[d])
        hero_winners.append(df['team dire 3p'].loc[d])
        hero_winners.append(df['team dire 4p'].loc[d])
        hero_winners.append(df['team dire 5p'].loc[d])
    d += 1


pickrate = []
all_heroes_test = Counter(all_heroes)
for v in sorted(all_heroes_test):
    pickrate.append(round(all_heroes_test[v] / (len(all_heroes) / 1000), 2))
AH = list(set(all_heroes))
AH.sort()


winrate = []
winners_heroes = Counter(hero_winners)
for i in sorted(all_heroes_test):
    winrate.append(round((winners_heroes[i] * 100) / all_heroes_test[i], 2))


df_1 = pd.DataFrame({'hero' : AH,
                     'pickrate' : pickrate,
                     'winrate' : winrate})

df_1.to_excel('2.xlsx')







