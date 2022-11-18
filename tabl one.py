import pandas as pd


pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv(r'D:\Users\I.Nokhrin\Downloads\hero_stats.csv',delimiter =',',quotechar =' ')


df = df.drop(['Hero Icon', 'Health Regen', 'Agility', 'Agility Gain', 'Intelligence', 'Intelligence Gain', 'Strength', 'Strength Gain', 'Mana Regen', '%Physical Damage Reduction'], axis= 1)
print(df)
# df.drop(columns=['Lifesteal'], axis= 1)
