# 3. Write a Python program to display the Fibonacci series

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
