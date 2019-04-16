# Clear all
clear_all()

# Standard import packages/modules

import pandas as pd
import os
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import glob



# Check and change working directory
os.getcwd()
#os.chdir('/Users/Leijtenss/PycharmProjects/MK8')

# Check which files are in working directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

print(files)
del files

# Import multiple csvs, combine into list for easy access
# Could've done this with a dictionary too, maybe
path = os.getcwd()

allFiles = glob.glob(path + "/*.csv")
filenames = glob.glob("*.csv")
dfs = [pd.read_csv(file) for file in allFiles]


# Still haven't figured out how to assign them automatically to separate dfs

bodies = pd.DataFrame(dfs[0])
tires = pd.DataFrame(dfs[1])
df_kk = pd.DataFrame(dfs[2])
characters = pd.DataFrame(dfs[3])
gliders = pd.DataFrame(dfs[4])

# Check unique values for certain columns
print(df_kk.groupby('characters')['characters'].nunique())


plt.clf()
plt.hist(x='total', data=df_kk, bins=10, edgecolor = 'black')
plt.xlabel('total')
plt.ylabel('number of combinations')
plt.show()



# Get some quick descriptives
# Play around with some histogram-graphs

# Using both matplotlib and sns
# sns.distplot(df_train['SalePrice'])
df_kk.columns
df_kk['weight'].describe()
df_kk['total'].describe()

np.std(df_kk['total'])


plt.clf()
sns.distplot(df_kk['weight'])
plt.show()

plt.clf(
plt.hist(df_kk['weight'], color = 'grey', edgecolor = 'black')
plt.show()
plt.clf()

# Let's check out how acceleration and speed are related
plt.scatter(df_kk['acceleration'], df_kk['speed'])
plt.xlabel('accel')
plt.ylabel('spd')
plt.show()

plt.clf()
sns.pairplot(x_vars=['acceleration'], y_vars=['speed'], data=df_kk, hue="weight", height=10)


# Plot looks a bit weird, hard to categorize speed_acc combinations
# Need to add weight-category to the df_kk-dataframe
# Example code: pandas.merge(df1, df2, how='left', left_on=['id_key'], right_on=['fk_key'])

# First, extract single character from characters in df_kk
df_kk['Character'] = df_kk['characters'].str.split(',').str[0]

# Then merge dataframes
#df_kk1 = pd.merge(df_kk, characters[['Character', 'Class']], how='left', left_on=['key'], right_on=['Character'])

# Problem with several grouped characters, check which ones first
#df2 = df_kk1[df_kk1['Class'].isnull()]
#print(df2.groupby('characters')['characters'].nunique())
#del df2

# Recode these grouped characters
# Baby Mario/Luigi, Dry Bones = Baby Mario
# Cat Peach, Inkling Girl, Villager Girl = Peach
# Link, King Boo, Rosalina    = Rosalina
# Metal/Gold Mario, Pink Gold Peach = Metal Mario
# Tanooki Mario, Inkling Boy, Villager Boy = Mario

df_kk['key'] = 0
df_kk['key'] = np.where(df_kk['characters'] == 'Baby Mario/Luigi, Dry Bones', 'Baby Mario', df_kk['Character'])
df_kk['key'] = np.where(df_kk['characters'] == 'Cat Peach, Inkling Girl, Villager Girl', 'Peach', df_kk['key'])
df_kk['key'] = np.where(df_kk['characters'] == 'Link, King Boo, Rosalina', 'Rosalina', df_kk['key'])
df_kk['key'] = np.where(df_kk['characters'] == 'Metal/Gold Mario, Pink Gold Peach', 'Metal Mario', df_kk['key'])
df_kk['key'] = np.where(df_kk['characters'] == 'Tanooki Mario, Inkling Boy, Villager Boy', 'Mario', df_kk['key'])


# Redo the merge
#df_kk1 = pd.merge(df_kk, characters[['Character', 'Class']], how='left', left_on=['key'], right_on=['Character']

# Then merge dataframes
df_kk1 = pd.merge(df_kk, characters[['Character', 'Class']], how='left', left_on=['key'], right_on=['Character'])


# Check how the merge went
#df_kk.columns
#df_kk1.columns


plt.clf()
sns.pairplot(x_vars='acceleration', y_vars='speed', data=df_kk1, hue="Class", height=5)


# Let's see if we can recreate this graph for karts with total larger than mean + 1 standard dev
filt_crit = (np.std(df_kk1['total'])) + np.mean(df_kk1['total'])
df_kk_filt = df_kk1[df_kk1['total'] > filt_crit]

plt.clf()
sns.pairplot(x_vars='acceleration', y_vars='speed', data=df_kk_filt, hue="Class", height=5)

# Check combination where speed = 3 and acc > 4.5 (light buggy)
filt_crit_opt = ((df_kk_filt['acceleration'] >= 4.5) & (df_kk_filt['speed'] == 3))

df_kk_opt = df_kk_filt[(df_kk_filt['acceleration'] >= 4.5) & (df_kk_filt['speed'] == 3)]


# Continue with just one dataframe, df
df = df_kk1

del df_kk
del df_kk_filt
del df_kk_opt
del df_kk1
del dfs
del filenames
del filt_crit_opt
del filt_crit
del path

