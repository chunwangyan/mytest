#import the necessery library
import pandas as pd


raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}


data1 = pd.DataFrame(raw_data_1, columns = ['subject_id', 'first_name', 'last_name'])
data2 = pd.DataFrame(raw_data_2, columns = ['subject_id', 'first_name', 'last_name'])
data3 = pd.DataFrame(raw_data_3, columns = ['subject_id','test_id'])

# print(data3.info())
# print(data3.describe())


#
# data3['subject_id'] = data3['subject_id'].astype(int)
#
# data3_max = data3.max(axis=0)
#
# print(data3_max)


# data1_data2_0 = pd.concat([data1,data2])
#
# data1_data2_1 = pd.concat([data1,data2],axis=1)
# print(data1_data2_0)
#
# print('--------------------')
#
# print(data3)
#
# data_merge = pd.merge(data1_data2_0,data3,on='subject_id')
#
# print(data_merge)


# inner join outer join

data_innerjoin = pd.merge(data1,data2,on='subject_id',how='inner')
data_outerjoin = pd.merge(data1,data2,on='subject_id',how='outer')
data_leftjoin = pd.merge(data1,data2,on='subject_id',how='left')
data_rightjoin = pd.merge(data1,data2,on='subject_id',how='right')
print(data1)
print('--------------------')
print(data2)
print('--------------------')
print(data_innerjoin)
print('--------------------')
print(data_outerjoin)
print('--------------------')
print(data_leftjoin)
print('--------------------')
print(data_rightjoin)




