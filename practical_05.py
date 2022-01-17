# 5. Write a Python Program to print first prime number.

num = int(input("Enter range:"))

for i in range(2, num):
    if num % i == 0:
        print(num, "Not a Prime")
        break
else:
    print(num, "is a prime")

# numr = int(input("Enter range:"))

# print("Prime numbers:", end=" ")
# for n in range(1, numr):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n, end=" ")
