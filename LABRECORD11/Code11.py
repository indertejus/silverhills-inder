# Write a python program to print the following pattern using while loop
# 1
# 12
# 123
# 1234
# 12345

num=int(input("Enter the rows upto which the number is to be printed: "))
i=1
while(i<=num):
    j=1
    while(j<=i):
        print(j, end=" ")
        j+=1
    print()
    i=i+1