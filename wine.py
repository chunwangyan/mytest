import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
wine = pd.read_csv(url)

wine = wine.drop(wine.columns[[0, 3, 6, 8, 11, 12, 13]], axis=1)
wine.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']

print(wine.head(3))

wine.iloc[0:3, 0] = np.nan
wine.iloc[2:4, 3] = np.nan

print(wine.head(10))

wine.alcohol.fillna('aa', inplace=True)
wine.magnesium.fillna('bb', inplace=True)

print(wine.head(20))

random = np.random.randint(0, 5, 10, int)
# rand = np.random.randint(1,10,10,int)
print(random)

wine.alcohol[random] = np.nan
print(wine.head(10))

print (wine.isnull().sum())

print (wine.alcohol[wine.alcohol.notnull()])

print(wine.reset_index(drop = True))