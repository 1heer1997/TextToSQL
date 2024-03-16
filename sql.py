import sqlite3

## connection sqlite

connection=sqlite3.connect("student.db")

## create a cursor object to insert record, create table, retrieve

cursor = connection.cursor()

drop="""
drop table STUDENT;
"""
cursor.execute(drop)

## create the table

table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## insert some more records

cursor.execute(''' Insert Into STUDENT values('Heer','DATA SCIENCE','A',99) ''')
cursor.execute(''' Insert Into STUDENT values('Sudhanshu','DATA SCIENCE','B',80) ''')
cursor.execute(''' Insert Into STUDENT values('Kush','DEVOPS','A',59) ''')
cursor.execute(''' Insert Into STUDENT values('Krish','DATA SCIENCE','B',45) ''')
cursor.execute(''' Insert Into STUDENT values('Dipak','DEVOPS','A',30) ''')
cursor.execute(''' Insert Into STUDENT values('Jigisha','COMPUTER SCIENCE','C',89) ''')
cursor.execute(''' Insert Into STUDENT values('Shobhit','DEVOPS','A',78) ''')
cursor.execute(''' Insert Into STUDENT values('Rohan','HIS','A',80) ''')
cursor.execute(''' Insert Into STUDENT values('Priya','HIS','B',60) ''')

## display all the records

print("The inserted records are")

data=cursor.execute(''' Select * From STUDENT''')

for row in data:
    print(row)

## close the connection
    
connection.commit()
connection.close()