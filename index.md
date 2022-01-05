## 1. Write a Python program to display 'Hello World" Message on Screen

```python
print("Hello World")
```

## 2. Write a Python program to swap two variables
```python
p = 5
q = 10

temp = p  # Now temp value is = 5
p = q   # Now temp value is p = 10
q = temp  # Now temp value is q = 5

print("The p value is : ", p)
print("The q value is : ", q)
```

## 3. Write a Python program to display the Fibonacci series
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

## 4. Write a Python program to calculate sum of given number.
```python
num1 = int(input("Enter a First Number : "))
num2 = int(input("Enter a Second Number : "))

sum = num1 + num2

print(sum)
```

## 5. Write a Python Program to print first prime number.
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
## 6. Write a Python Program to Check Armstrong Number.
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

### 7. Write a Python Program to Create a sequence of numbers using range datatype to display 1 to 30, with an increment of 2.
```python
"""
range(start, stop, step)
https://www.w3schools.com/python/ref_func_range.asp
"""

x = range(1, 30, 2)
for n in x:
    print(n)
```

## 8. Write a Python Program to Find area of circle.
```python
PI = 3.14
r = float(input("Enter the radius of a circle : "))
area = PI * r * r
print("Area of a circle = %.2f" % area)
```
## 9. Write a Python program to implement Factorial series up to user entered number.
```python
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("The factorial of", num, "is", factorial)
```

## 10. Write a Python program to check the given number is palindrome or not.
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
