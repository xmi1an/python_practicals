# 22.Write a Python program for Error Handling.

try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    c = a/b
    print("Division is : ", c)
except:
    print("Can't divide with zero")
