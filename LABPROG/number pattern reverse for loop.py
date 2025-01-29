r= int(input("Enter: "))
for i in range (r+1):
    for j in range(1, r+1, 1):
        print(j, end=" ")
    r-=1
    print()
