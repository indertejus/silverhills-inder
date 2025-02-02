# WRITE A PYTHON PROGRAM TO EVALUATE THE FOLLOWING SERIES
# 1-x+x2-x3+....+xn

x=int(input("Enter the base(x): "))
n=int(input("Enter the power(n): "))
sum=0
for i in range(n+1):
    if(i%2==0):
        sum=sum+x**i
    else:
        sum=sum-x**i
print("The result of the series is:", sum)
