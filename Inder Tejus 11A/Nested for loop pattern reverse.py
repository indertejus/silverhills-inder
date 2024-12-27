rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(0, rows, 1):
        print("*", end=" ")
    rows = rows-1
    print()
