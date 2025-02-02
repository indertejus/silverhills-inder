# Write a python program to print the following pattern
# using for loop
# A
# AB
# ABC
# ABCD
# ABCDE

rows = int(input("Enter the no. of rows upto which the letters to be printed: "))
for i in range(rows):
    for j in range(i+1):
        print(chr(j+65), end=" ")
    print()
