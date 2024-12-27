## program to print the pattern using while loop

rows = int(input("Enter the number of rows: "))
i=1
while (i<=rows):
    j=1
    while (j<=i):
        print("*", end=" ")
    j+=1
    print()
    i+=1
