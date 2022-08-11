import mysql.connector as conn
import pandas as pd
import warnings
import pymongo
import json

warnings.filterwarnings('ignore')
mydb = mydb = conn.connect(host="localhost", user="root", passwd="root")
print(mydb)

##Task 3. Read these datasets in pandas as a dataframe
sql1 = pd.read_sql('select count(*) from ineuron.Attribute_DataSet', mydb)
attribute_data = pd.DataFrame(sql1, columns=['dress_id', 'style', 'price', 'rating', 'size', 'season', 'neckline',
                                             'sleevelength', 'waiseline', 'material', 'fabrictype', 'decoration',
                                             'patterntype', 'recommendation'])
print(attribute_data)
sql2 = pd.read_sql('select count(*) from ineuron.dress_sales', mydb)

dress_sales = pd.DataFrame(sql2, columns=['dress_id', '29/8/2013', '31/8/2013', '2/9/2013', '4/9/2013', '6/9/2013',
                                          '8/9/2013', '10/9/2013',
                                          '12/9/2013', '14/9/2013', '16/9/2013', '18/9/2013', '20/9/2013', '22/9/2013',
                                          '24/9/2013'
    , '26/9/2013', '28/9/2013', '30/9/2013', '2/10/2013', '4/10/2013', '6/10/2013',
                                          '8/10/2013', '10/10/2013', '12/10/2013'])
print(dress_sales)

####Task 4. Convert Attribute Dataset in JSON Format (.to_json will be used)


attribute_data_json = attribute_data.to_json()
print(attribute_data_json)

# Task 5. Store this json dataset into mongodb (Insert_many will be used)

from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("mongodb+srv://root:root@rajancluster0.ub5nt.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['Task']

collection = database["Json"]
print(attribute_data_json)

# storing json data into Mongo db

with open(r'C:\Users\Rajan\Attribute Data_JSON') as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    collection.insert_many(file_data)
else:
    collection.insert_one(file_data)

# Task 6. In SQL task, try to perform left join operation with Attribute dataset and dress dataset on column Dress_ID

left_join = pd.merge(attribute_data, dress_sales, how='left', on='dress_id')
print(left_join)

#Task 7. Write the SQL query to find out how many unique dress that we have based on Dress_ID

cursor = mydb.cursor()
cursor.execute("select count(distinct(dress_id)) from ineuron.attribute_dataset")
for i in cursor.fetchall():
    print(i)
#output is 475




