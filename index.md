BCA-603 : Python Programming (Practical) (1-25)

#### [Download zip🙂](https://github.com/xmi1an/python_practicals/archive/refs/heads/master.zip)

#### 🌟 How to run programs :

1. Clone or [download](https://github.com/xmi1an/python_practicals/archive/refs/heads/master.zip) this repo to your computer.
2. Unzip (If you download zip).
3. Open "Python-Programs" folder.
4. Run programs using cmd or any python IDE.

---


### Practical 1
Write a Python program to display 'Hello World" Message on Screen.
```python
print("Hello World")
```

### Practical 2
Write a Python program to swap two variables.
```python
p = 5
q = 10

temp = p  # Now temp value is = 5
p = q   # Now temp value is p = 10
q = temp  # Now temp value is q = 5

print("The p value is : ", p)
print("The q value is : ", q)
```

### Practical 3
Write a Python program to display the Fibonacci series.
```python
# Define a Function
def fibonacci(n):
    first_value = 0
    second_value = 1
    if(n == 1):
        print(first_value)
    else:
        print(first_value)
        print(second_value)
        for i in range(2, n):
            next = first_value + second_value
            first_value = second_value
            second_value = next
            print(next)


# Calling fib function
fibonacci(10)
```

### Practical 4
Write a Python program to calculate sum of given number.
```python
num1 = int(input("Enter a First Number : "))
num2 = int(input("Enter a Second Number : "))

sum = num1 + num2

print(sum)
```

### Practical 5
Write a Python Program to print first prime number.
```python
numr = int(input("Enter range:"))

print("Prime numbers:", end=' ')
for n in range(1, numr):
    for i in range(2, n):
        if(n % i == 0):
            break
    else:
        print(n, end=' ')
```
### Practical 6
Write a Python Program to Check Armstrong Number.
```python
n = int(input("Enter a number: "))
# initialize the sum
s = 0
t = n

while t > 0:
    digit = t % 10
    s += digit ** 3
    t //= 10

# display the result
if n == s:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
```

### Practical 7
Write a Python Program to Create a sequence of numbers using range datatype to display 1 to 30, with an increment of 2.
```python
"""
range(start, stop, step)
https://www.w3schools.com/python/ref_func_range.asp
"""

x = range(1, 30, 2)
for n in x:
    print(n)
```

### Practical 8
Write a Python Program to Find area of circle.
```python
PI = 3.14
r = float(input("Enter the radius of a circle : "))
area = PI * r * r
print("Area of a circle = %.2f" % area)
```
## Practical 9
Write a Python program to implement Factorial series up to user entered number.
```python
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("The factorial of", num, "is", factorial)
```

## Practical 10
Write a Python program to check the given number is palindrome or not.
```python
n = int(input("Enter number:"))
temp = n
rev = 0

while(n > 0):
    dig = n % 10
    rev = rev*10+dig
    n = n//10

if(temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
```
## Practical 11
```python
# 11. Write a python program to display ascending and descending order from given 10 numbers.
"""
- The sort() method sorts the list ascending by default.
- reverse Optional. reverse=True will sort the list descending. Default is reverse=False
https://www.w3schools.com/python/ref_list_sort.asp
"""

numbers = [1, 3, 4, 2, 7, 10, 8, 5, 9, 6]

# Sorting list of Integers in ascending.
numbers.sort()
print(numbers)

# Sorting list of Integers in descending.
numbers.sort(reverse=True)
print(numbers)
```
## Practical 12
```python
# 12.Write a Python program to print the duplicate elements of an myarrayay.

myarray = [1, 9, 3, 4, 2, 7, 8, 8, 9, 3]

print("Duplicate elements in given myarrayay : ")

for i in range(0, len(myarray)):
    for j in range(i + 1, len(myarray)):
        if(myarray[i] == myarray[j]):
            print(myarray[j])
```
## Practical 13
```python
# 13.Write Python programs to create functions and use functions in the program.
"""
- A function can be defined as the organized block of reusable code, which can be called whenever required.
- Python provides the def keyword to define the function. 
https://www.javatpoint.com/python-functions
"""

# function definition


def msg():
    print("Hello Peter")


def sum(a, b):
    print(a + b)


# function calling
msg()
sum(5, 2)
```
## Practical 14
```python
# 14. Write Python programs to using lambda function.
"""
Python Lambda function is known as the anonymous function that is defined without a name. Python allows us to not declare the function in the standard manner, i.e., by using the def keyword. Rather, the anonymous functions are declared by using the lambda keyword. However, Lambda functions can accept any number of arguments, but they can return only one value in the form of expression.
https://www.javatpoint.com/python-lambda-functions
"""

# a is an argument and a+10 is an expression which got evaluated and returned.    
x = lambda a:a+10   

# Here we are printing the function object  
print(x)  
print("sum = ",x(20))   
```
## Practical 15
```python
# 15. Write Python programs Loading the module in Python code.
"""
A python module can be defined as a python program file which contains a python code including python functions, class, or variables. In other words, we can say that our python code file saved with the extension (.py) is treated as the module. We may have a runnable code inside the python module.
https://www.javatpoint.com/python-modules
"""

# Part 1 of Practical 15.
# Saved as practical_15.py

import practical_15part2

practical_15part2.greeting("Peter")
```

## Practical 15 Part 2
```python
# 15. Write Python programs Loading the module in Python code.
# Part 2 of Practical 15.
# Saved as practical_15part2.py

def greeting(name):
    print("Hello, " + name)

# end of part 2.
```
## Practical 16
```python
# 16.Write a program to print following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = 5

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
```
## Practical 17
```python
# 17. Write Python programs to implement a concept of list.
"""
A list in Python is used to store the sequence of various types of data. Python lists are mutable type its mean we can modify its element after it created. However, Python consists of six data-types that are capable to store the sequences, but the most common and reliable type is the list.
A list can be defined as a collection of values or items of different types. The items in the list are separated with the comma (,) and enclosed with the square brackets [].
https://www.javatpoint.com/python-lists 
"""
avengers = ["Ironman", "Spiderman", "Hulk", "Wanda", "Hawkeye", "Natasha"]

print(avengers)

# prints the object's type
print(type(avengers))

# prints 2nd element (Hulk)
print(avengers[2])

# Slicing the elements
print(avengers[1:4])

# update the values
avengers[2] = "Vision"
print(avengers)
```
## Practical 18
```python
# 18. Write Python programs to implement a concept of tuples.
"""
Python Tuple is used to store the sequence of immutable Python objects. The tuple is similar to lists since the value of the items stored in the list can be changed, whereas the tuple is immutable, and the value of the items stored in the tuple cannot be changed.
https://www.javatpoint.com/python-tuples
"""

avengers = ("Ironman", 3000, True, "Wanda", "Hawkeye")
print(avengers)
print(type(avengers))
```
## Practical 19
```python
# 19.Write a Python program to create nested list and display its elements.
"""
Nested List Comprehensions are nothing but a list comprehension within another list comprehension which is quite similar to nested for loops.
https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
"""

mynumbers = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
]

for list in mynumbers:
    for number in list:
        print(number, end=' ')
```
## Practical 20
```python
# 20.Write a Python program to using multiple inheritance.
"""
Multiple Inheritance 
When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.
https://www.geeksforgeeks.org/multiple-inheritance-in-python/
"""


class Class1:
    def msg1(self):
        print("In Class1")


class Class2(Class1):
    def msg2(self):
        print("In Class2")


class Class3(Class1):
    def msg3(self):
        print("In Class3")


class Class4(Class2, Class3):
    def msg(self):
        print("In Class4")


obj = Class4()
obj.msg1()
```
## Practical 21
```python
# 21. Write a Python program to read a file bca.txt and print the contents of file along with number of vowels present in it.
"""
- The open() function takes two parameters; filename, and mode.
- To open the file, use the built-in open() function.
- The open() function returns a file object, which has a read() method for reading the content of the file:
https://www.w3schools.com/python/python_file_open.asp
"""

myfile = open("./practical_21part2.txt", "r")
read_data = myfile.read()

# find the number of the vowels in file

vowel_count = 0
for i in read_data:
    if(i == 'A' or i == 'a' or i == 'E' or i == 'e' or i == 'I'
        or i == 'i' or i == 'O' or i == 'o'
            or i == 'U' or i == 'u'):
        vowel_count += 1

print('The Number of Vowels in text file :', vowel_count)

myfile.close()
```
## Practical 21 Part 2
```python
practical_21part2.txt
Lorem ipsum dolor sit amet.
```
## Practical 22
```python
# 22.Write a Python program for Error Handling.
"""
- The try block lets you test a block of code for errors.
- The except block lets you handle the error.
- The finally block lets you execute code, regardless of the result of the try- and except blocks.
https://www.w3schools.com/python/python_try_except.asp
"""
try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    c = a / b
    print("Division is : ", c)
except:
    print("Can't divide with zero")
finally:
    print("Rest of the code..")
```
## Practical 23
```python
# 23. Write a Python program for connection with my Sql and display all record from the database.
"""
- We need "MySQL Connector" module to access MySQL databases.
- To install "MySQL Connector" Open cmd and type following :
python -m pip install mysql-connector-python
- Next Open xamp or wamp and start MySQL Server and create database.
- Create users Table and add dummy data.
-https://www.w3schools.com/python/python_mysql_getstarted.asp
"""
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', database='test', user='root', password='')

mycursor = mydb.cursor()

sql = "SELECT * FROM users"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
```
## Practical 24
```python
# 24. Write a Python program for modified record, display record and delete record from the database.
"""
- We need "MySQL Connector" module to access MySQL databases.
- To install "MySQL Connector" Open cmd and type following :
python -m pip install mysql-connector-python
- Next Open xamp or wamp and start MySQL Servel and create "test" database.
- Create users Table and add dummy data.
-https://www.w3schools.com/python/python_mysql_getstarted.asp
"""

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    database='test',
    user='root',
    password=''
)

mycursor = mydb.cursor()

updatesql = "UPDATE users SET city = 'Baroda' WHERE city = 'Idar'"
deletesql = "DELETE * FROM users where city = 'idar'"

mycursor.execute(updatesql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
```
## Practical 25
```python
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
mydb = mysql.connector.connect(
    host='localhost',
    database='test',
    user='root',
    password=''
)

mycursor = mydb.cursor()
search = input("Search : ")

sql = "SELECT * FROM users WHERE name='%s' " % search

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
```
