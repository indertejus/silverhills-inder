# Write a python program to print the following pattern using while loop
# 12345
# 1234
# 123
# 12
# 1

num=int(input("Enter the number uptil which to be printed:"))
i=num
while(i>=0):
    j=1
    while(j<=i):
        print(j, end=" ")
        j=j+1
    print()
    i=i-1