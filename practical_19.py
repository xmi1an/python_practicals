# 19.Write a Python program to create nested list and display its elements.

mynumbers = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
]

for list in mynumbers:
    for number in list:
        print(number, end=' ')
