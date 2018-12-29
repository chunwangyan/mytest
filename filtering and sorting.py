#import the resources
import pandas as pd
import numpy as np

#set print parameter
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url,sep='\t')


# look head 5 rows data
# print(chipo.head(5))

# converse the prince to float type
prices = [float(value[1:]) for value in chipo.item_price]

chipo.item_price = prices

# print(chipo.info())

#duplicates some data
chipo_filtering = chipo.drop_duplicates(['quantity','item_name'])
# print(chipo_filtering.info())


#select the products the quantity = 1
chipo_one_prod = chipo_filtering[chipo_filtering.quantity == 1]
# print(chipo_one_prod)

print(chipo_one_prod[chipo_one_prod['item_price']>10].item_name.nunique())

#sort the data
price_per_item = chipo_one_prod[['item_name','item_price']]
price_per_item_top10 = price_per_item.sort_values(by = 'item_price', ascending=False).head(10)
print(price_per_item_top10)


#sum the condation data
chipo_drink_steak_bowl = chipo[(chipo.item_name == 'Canned Soda') & (chipo.quantity > 1)]
print(chipo_drink_steak_bowl)
print(len(chipo_drink_steak_bowl))


print(chipo_drink_steak_bowl[['order_id','item_name']])






