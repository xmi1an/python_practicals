# 25. Write a Python program for search record from the database.
"""
- We need "MySQL Connector" module to access MySQL databases.
- To install "MySQL Connector" Open cmd and type following :
python -m pip install mysql-connector-python
- Next Open xamp or wamp and start MySQL Servel and create "test" database.
- Create users Table and add dummy data.

-https://www.w3schools.com/python/python_mysql_getstarted.asp
"""

import mysql.connector
print("")
mydb = mysql.connector.connect(
    host='localhost', database='test', user='root', password='')

mycursor = mydb.cursor()
sql = "SELECT * FROM users WHERE city ='Baroda'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
