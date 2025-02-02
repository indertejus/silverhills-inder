# Write a program to check whether the given number is
# prime number or not.

num=int(input("Enter the number: "))
flag=False
if num>=2:
    if(num==2):
        print(num, "is a prime number.")
    else:
        for i in range(2,num):
            if (num%i==0):
                flag=True
                break
        if flag==False:
            print(num, "is a prime number.")
        else: print(num, "is not a prime number")
else: print("The entered number is not prime.")
