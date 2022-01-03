# 21. Write a Python program to read a file bca.txt and print the contents of file along with number of vowels present in it.

# open file in read mode
myfile = open("./bca.txt", "r")

# read all the contents of file
# and store in a string variable
# named read_data using read() function

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
