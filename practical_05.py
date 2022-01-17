# 5. Write a Python Program to print first prime number.


for n in range(1, 20):
    for i in range(2, n):
        if n % i == 0:
            print("Prime Number is :", n)
            break
    else:
        pass

# numr = int(input("Enter range:"))

# print("Prime numbers:", end=" ")
# for n in range(1, numr):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n, end=" ")
