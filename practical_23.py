# 23. Write a Python program for connection with my Sql and display all record from the database.

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', database='test', user='root', password='')

mycursor = mydb.cursor()

sql = "SELECT * FROM users"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
