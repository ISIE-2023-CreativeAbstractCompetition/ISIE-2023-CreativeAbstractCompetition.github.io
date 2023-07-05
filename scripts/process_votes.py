#%%

import pandas as pd

# Read in the data
df_raw = pd.read_csv('/home/stew/code/gh/ISIE/ISIE-2023-CreativeAbstractCompetition.github.io/.secret/Voting - Creative Abstract Competition - ISIE 2023.csv')

# Filter the columns
df = df_raw.filter(regex='^Your')

one = df.value_counts("Your favourite?")*3
two = df.value_counts("Your second favourite?")*2
three = df.value_counts("Your third favourite?")


# Combine the votes
votes = pd.DataFrame({"one": one, "two": two, "three": three}).fillna(0)
votes['onetwo'] = votes['one'] + votes['two']
votes['onetwothree'] = votes['one'] + votes['two'] + votes['three']
votes = votes.astype(int).sort_values('onetwothree', ascending=False)
# votes.drop(columns=['two', 'three'], inplace=True)
votes['total'] = votes['one'] + votes['two'] + votes['three']
votes = votes.astype(int).sort_values('total', ascending=False)
# votes = votes.iloc[:6]
votes.drop(columns=['total', 'two', 'three'], inplace=True)
# votes['name'] = votes.index

# abbreviate names, taking first name, skipping Dr.
votes.index = votes.index.str.replace('Dr. ', '')
votes.index = votes.index.str.split(' ').str[0]
votes.columns = votes.columns.map({'one': '1st choice', 'onetwo': '1st + 2nd choice', 'onetwothree': 'Total'})
votes.to_csv('../.secret/votes.csv')


#%% bar raceimport pandas as pd
import pandas as pd
import bar_chart_race as bcr

# Read in the data
df = pd.read_csv('../.secret/votes.csv', index_col=0)
df[" Total"] = df["Total"]
df[" 1st choice"] = df["1st choice"]
df = df.reindex(columns=[" 1st choice", "1st choice", "1st + 2nd choice", "Total", " Total"])

# Define the color map
colors = ["#DA003F",  "#043C4D", "#ADBF2B", "#DA9B00", "#A33656", "#085972"]
colors_dict = {person: color for person, color in zip(df.index, colors)}
bar_label_kwargs = {'fontsize': 20, 'color': 'white', 'weight': 'bold'}

# Create the bar chart race
bcr.bar_chart_race(df.T, 
                   cmap=colors, 
                   steps_per_period=1000, 
                   period_length=3000, 
                   figsize=(16, 12),
                   bar_label_size=35,
                   tick_label_size = 35,
                   filename='../.secret/total_votes.mp4',
                   period_label = {'x': .99, 'y': .2, 'ha': 'right', 'va': 'center', 'fontsize': 45, 'color': 'black', 'weight': 'bold'},
)