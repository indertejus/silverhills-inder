# Write a python program to evaluate the following series
# x+x2/2+x3/3+.....xn/n

x=int(input("Enter the base(x): "))
n=int(input("Enter the power(n): "))

sum=0
for i in range (1, n+1):
    sum=sum+((x**i)/i)
print("The result of the series is: ",sum)
