import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (15,8)


df = pd.read_csv("matches.csv")
dummy = pd.get_dummies(df['toss_decision'])
df = pd.concat([df,dummy], axis=1)
print(df.head())
print(df.shape)
print(df.info())
print(df.columns)
print(df.nunique(axis=0))
print(df.describe().apply(lambda s: s.apply(lambda x: format(x, 'f'))))

df_winneres = df.winner.value_counts()
fig, ax = plt.subplots()
ax.set_ylabel("Team")
ax.set_xlabel("No. of matches won")
sns.barplot(y=df_winneres.index, x=df_winneres, orient='h')
plt.show()

df_top_players = df.player_of_match.value_counts()[:15]
fig, ax = plt.subplots()
ax.set_ylim([0,23])
ax.set_ylabel("Count")
ax.set_title("Most significant player")
sns.barplot(x=df_top_players.index, y=df_top_players, orient='v')
plt.show()


factor = df['toss_winner'] == df['winner']
print(factor.groupby(factor).size())
sns.countplot(factor)
plt.show()
