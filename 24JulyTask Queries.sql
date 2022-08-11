##--Task 2 Do a bulk load for these 2 tables for respective dataset in mysql workbench/python
use ineuron;

LOAD DATA INFILE 'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\Attribute DataSet.csv' INTO TABLE ineuron.attribute_dataset
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

select * from ineuron.attribute_dataset;



LOAD DATA INFILE 'C:/Program Files/MySQL/Dress Sales.csv' INTO TABLE ineuron.dress_sales
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

select * from ineuron.dress_sales;
show columns from ineuron.dress_sales;


## Task 8 Try to find out how many dress is having recommendation as 0
select count(dress_id) as count_recommendation from ineuron.attribute_dataset where recommendation =0;
##output 290

## Task 9 Try to find out total dress sales for each and every Dress_ID
## Task 10 Try to find out the third highest most selling Dress_ID

select dress_id,`29/8/2013`,`31/8/2013`,`2/9/2013`,`4/9/2013`,`6/9/2013`,`8/9/2013`,`10/9/2013`,`12/9/2013`,`14/9/2013`,`16/9/2013`,`18/9/2013`,`20/9/2013`,`22/9/2013`,`24/9/2013`,`26/9/2013`,`28/9/2013`,`30/9/2013`,`2/10/2013`,`4/10/2013`,`6/10/2013`,`8/10/2013`,`10/10/2013`,`12/10/2013`,
	(`29/8/2013` + `31/8/2013` + `2/9/2013` + `4/9/2013` + `6/9/2013` + `8/9/2013` + `10/9/2013` + `12/9/2013` + `14/9/2013` + `16/9/2013` + `18/9/2013` + `20/9/2013` + `22/9/2013` + `24/9/2013` + `26/9/2013` + `28/9/2013` + `30/9/2013` + `2/10/2013` + `4/10/2013` + `6/10/2013` + `8/10/2013` + `10/10/2013` + `12/10/2013`) 
    as Total_sales from ineuron.dress_sales order by Total_sales desc limit 3;
