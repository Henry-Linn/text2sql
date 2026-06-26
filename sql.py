import sqlite3

## Connect to sqlite

connection=sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retrieve 
cursor = connection.cursor()

# Create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

## Insert some more records

cursor.execute('''Insert Into STUDENT values('A','Data Science','A',90 )''')
cursor.execute('''Insert Into STUDENT values('B','Data Science','B',100 )''')
cursor.execute('''Insert Into STUDENT values('C','Data Science','A',94 )''')
cursor.execute('''Insert Into STUDENT values('D','DEVOPS','B',23 )''')
cursor.execute('''Insert Into STUDENT values('F','DEVOPS','A',52 )''')

## Display all the records
print("The inserted records are")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)


## Close the connection
connection.commit()
connection.close()