# 10. Write a Python program to check the given number is palindrome or not.

n = int(input("Enter the number : "))
reverse = 0
number = n

# reversing the given numberwhile(n != 0):
remainder = n % 10
reverse = reverse * 10 + remainder

n = int(n / 10)

if(number == reverse):
    print("Palindrome")
else:
    print("Not a Palindrome")
