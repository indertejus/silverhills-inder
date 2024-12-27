x = int(input("Enter the base (x): "))
n = int(input("Enter the power (n): "))
sum=0
for i in range (1,n+1):
    sum = sum + ((x**i)/i)
print("Result: ", sum)
