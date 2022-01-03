# 25. Write a Python program for search record from the database.

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', database='test', user='root', password='')

mycursor = mydb.cursor()
sql = "SELECT * FROM users WHERE city ='Idar'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
