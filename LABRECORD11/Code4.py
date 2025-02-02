# Write a python program to print the following pattern
# using nested for loop
# *
# **
# ***
# ****
# *****
rows=int(input("Enter the number of rows: "))
for i in range (rows):
    for j in range(i+1):
        print("* ", end=" ")

    print()