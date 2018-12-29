#import the necessary libraries
import pandas as pd

#set print rules
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)


#import the dataset
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'

drinks = pd.read_csv(url,sep=',')

print(drinks.head(3))

# which continent drinks more beer on average
drinks_beer_average = drinks.groupby('continent').beer_servings.mean()
print(drinks_beer_average)


#for each continent print statistics
drinks_wine_statistic = drinks.groupby('continent').describe()
print(drinks_wine_statistic)


#print each continent columns median
drinks_each_median = drinks.groupby('continent').median()
print(drinks_each_median)


#print min max mean of spirit_servings
drinks_spirit_agg = drinks.groupby('continent').spirit_servings.agg(['min','max','mean'])
print(drinks_spirit_agg)