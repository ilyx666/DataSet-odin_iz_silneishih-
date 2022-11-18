import pandas as pd


pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
#для шараги
# df = pd.read_csv(r'D:\Users\I.Nokhrin\Downloads\hero_stats.csv',delimiter =',',quotechar =' ')
#для дома
df = pd.read_csv(r'C:\Users\ilyx\Downloads\hero_stats (1).csv',delimiter =',',quotechar =' ')

df = df.drop(['Hero Icon', 'Health Regen', 'Agility', 'Agility Gain', 'Intelligence', 'Intelligence Gain', 'Strength', 'Strength Gain', 'Mana Regen', '%Physical Damage Reduction', 'Turn Rate', 'Base Damage Min', 'Base Damage Max', 'Bonus Damage', 'Bonus Damage Reduction', 'Base Damage Average', 'Damage Min', 'Damage Max', 'Status Resistance', 'Magic Resistance', 'Base Attack Time', 'Increased Attack Speed', 'Attack Time', 'Attacks Per Second', 'Attack Point', 'Projectile Speed', 'Evasion', 'Physical Effective Health', 'Magical Effective Health', 'Bash Chance', 'Crit Chance', 'Miss Chance', 'Attack Range', 'Vision Range Day', 'Vision Range Night', 'Lifesteal', 'Attack Damage'], axis= 1)

print(df)
df.to_excel('output.xlsx')
# df.drop(columns=['Lifesteal'], axis= 1)
