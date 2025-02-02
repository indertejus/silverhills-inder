# Write a program to generate Fibonacci series upto a limit.

terms= int(input("Enter the number of terms: "))
f1,f2=0,1
count=0
n=0
if(terms<=0):
    print("Please enter a positive number.....")
else:
    while(count<terms):
        print(f1)
        n=f1+f2
        f1=f2
        f2=n
        count+=1

 
   
