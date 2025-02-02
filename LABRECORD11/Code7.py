# Write a python program to print the following pattern
# using while loop
# *****
# ****
# ***
# **
# *

rows = int(input("Enter the number of rows: "))
i=0
while (rows>0):
    i=1
    while(i<=rows):
        print("*", end=" ")
        i+=1
    print()
    rows-=1
