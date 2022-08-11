#1.Create a Table of attribute dataset and dress dataset in mysql workbench/python

import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="root")
print(mydb)

cursor = mydb.cursor()


s = "create table if not exists ineuron.Attribute_DataSet(dress_id int ,style varchar(30) ,price varchar(30) ,rating decimal (2,1) ,size varchar(30),season varchar(30),neckline varchar(30),sleevelength varchar(30) ,waiseline varchar(30) ,material varchar(30) ,fabrictype varchar(30) ,decoration varchar(30) ,patterntype varchar(30) ,recommendation int);"
cursor.execute(s)
## Attribute_DataSet table created

s2 = "create table if not exists ineuron.dress_sales (dress_id int ,`29/8/2013` int ,`31/8/2013` int ,`2/9/2013` int ,`4/9/2013` int ,`6/9/2013` int,`8/9/2013` int,`10/9/2013` int ,`12/9/2013` int ,`14/9/2013` int ,`16/9/2013` int ,`18/9/2013` int ,`20/9/2013` int ,`22/9/2013` int ,`24/9/2013` int ,`26/9/2013` int ,`28/9/2013` int ,`30/9/2013` int ,`2/10/2013` int ,`4/10/2013` int ,`6/10/2013` int ,`8/10/2013` int ,`10/10/2013` int ,`12/10/2013` int);"

cursor.execute(s2)
print(cursor.fetchall())