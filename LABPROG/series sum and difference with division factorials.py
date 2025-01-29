x = int(input("Enter x: "))
n = int(input("Enter n: "))
sum = 0
factorial = 1
for i in range(1, n+1):
    factorial*=i
    sum = sum +(x**i)/factorial
print("The result of the series is: ", sum)
