# Standard import packages/modules
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
#%matplotlib inline
import glob


# Check and change working directory
os.getcwd()
os.chdir('C:\\Users\\stelei\\Desktop\\03_MK8\\')

# Check which files are in working directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

print(files)
del files

# Start with importing csv-files and checking them out
df_KK = pd.read_csv('KartKross.csv')
df_KK.columns
df_KK.iloc[:,0].head(10)

# Check unique values for certain values
np.unique(df_KK['characters'])

# Loaded one df before
# Let's try and import every df in the working directory
del df_KK

# path = os.getcwd()
# files = glob.glob('*.csv')
# df_from_each_file = (pd.read_csv(f) for f in files)

bodies = pd.read_csv('bodies.csv')
char = pd.read_csv('characters.csv')
gliders = pd.read_csv('gliders.csv')
tires = pd.read_csv('tires.csv')

df_kk = pd.read_csv('KartKross.csv')

# Get some quick descriptives
# Play around with some histogram-graphs

# Using both matplotlib and sns
# sns.distplot(df_train['SalePrice'])
df_kk.columns
df_kk['weight'].describe()

sns.distplot(df_kk['weight'])
plt.show()
plt.clf()

plt.hist(df_kk['weight'], color = 'grey', edgecolor = 'black')
plt.show()
plt.clf()

# Let's check out how acceleration and speed are related
plt.scatter(df_kk['acceleration'], df_kk['speed'])
plt.xlabel('accel')
plt.ylabel('spd')
plt.show()

plt.clf()

sns.pairplot(x_vars=['acceleration'], y_vars=['speed'], data=df_kk, hue="weight", size=10)

# Plot looks a bit weird, hard to categorize speed_acc combinations
# Need to add weight-category to the df_kk-dataframe
# Example code: pandas.merge(df1, df2, how='left', left_on=['id_key'], right_on=['fk_key'])

df_kk1 = pd.merge(df_kk, char[['Weight', 'Class']], how='left', left_on=['weight'], right_on=['Weight'])

df_kk.columns
df_kk1.columns

sns.pairplot(x_vars='acceleration', y_vars='speed', data=df_kk1, hue="Class", size=5)
