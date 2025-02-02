# Write a python program to print the following number pattern
# using nested for loop
# 12345
# 1234
# 123
# 12
# 1

rows= int(input("Enter the number of rows: "))
for i in range (rows+1):
    for j in range(1, rows+1, 1):
        print(j, end=" ")
    rows-=1
    print()
