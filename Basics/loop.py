# While Loop
i = 1
while i < 6:
    print(i)
    i += 1

# Do While
i = 1

while True:
    print(i)
    i = i + 1
    if(i > 5):
        break

# Nested Loop
i = 1
while i <= 4:
    j = 0
    while j <= 3:
        print(i*j, end=" ")
        j += 1
    print()
    i += 1
