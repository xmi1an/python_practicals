# 24. Write a Python program for modified record, display record and delete record from the database.

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', database='test', user='root', password='')

mycursor = mydb.cursor()

sql = "UPDATE users SET city = 'Patan' WHERE city = 'Baroda'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
