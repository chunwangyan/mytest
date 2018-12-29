import pandas as pd

#set print rules
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

#read the dataset
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_table(url,sep='|',index_col='user_id')


#print some data rows
print(users.head(3))

#define an fuctuion and apply it
def gender_to_num(x):
    if x == 'M':
        return 1
    if x == 'F':
        return 0

users['gender_num'] = users['gender'].apply(gender_to_num)

# print(users.head(3))
r = users.groupby('occupation').gender_num.sum() / users.occupation.value_counts() *100

print(r.sort_values(ascending = False))



#grouping by age and print min and max

users_age = users.groupby('occupation').age.agg(['min','max','mean'])

print(users_age)


users_occupationandgender = users.groupby(['occupation','gender']).age.mean()

print(users_occupationandgender)

#calculate ratio of gerder group by occupation

gender_occup = users.groupby(['occupation','gender']).agg({'gender':'count'})

print(gender_occup)
occup_count = users.groupby(['occupation']).agg('count')

print(occup_count)
occup_gender = gender_occup.div(occup_count,level= "occupation") * 100

print(occup_gender.loc[:,'gender'])



#iterate print group by dataset
print('---------------------------------------------')
for name,group in users.groupby('occupation'):
    print(name)
    print(group)



# print(users.idxmax)







