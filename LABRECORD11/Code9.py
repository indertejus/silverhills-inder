# Write a python program to print the following number pattern
# using nested for loop
# 1
# 12
# 123
# 1234
# 12345
rows = int(input("Enter the number of rows: "))
for i in range (0, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()