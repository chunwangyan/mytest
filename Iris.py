import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url)

iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
print(iris.head(5))

print(pd.isnull(iris).sum())

iris.iloc[10:30, 2:3] = np.nan
print (iris.head(20))

iris.petal_length.fillna(1, inplace=True)
print (iris.head(20))

del iris['class']
print (iris.head(2))

iris = iris.dropna(how='any')
print(iris.head(20))
