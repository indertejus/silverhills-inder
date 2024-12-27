# Write a program to check whether the given number is Palindrome number, perfect number or Armstrong number.

#Function to check if a number is an Perfect number
def is_perfect_number(num):
    sum_of_divisors=0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors +=i
    return sum_of_divisors==num

# Function to check if a number is an Armstrong number
def is_armstrong_number(num):
    order = len(str(num))
    temp = num
    sum = 0
    while temp >0:
        digit = temp % 10
        sum += digit ** order
        temp //=10
        print(temp)
    return sum==num

# Function to check if a number is a palindrome
def is_palindrome(num):
    temp = num
    sum = 0
    while temp>0:
        digit = temp % 10
        sum = sum*10+digit
        print("Sum is" ,sum)
        temp//=10
        print(temp)
    return sum==num
    # return str(num) == str(num)[::-1]

# input a number from the user
number = int(input("Enter a number: "))

# Check if the number is a perfect number
if is_perfect_number(number):
    print(number, "is a perfecct number.")
else: print(number, "is not a perfect number.")

# Check if the number is an Armstrong numbr
if is_armstrong_number(number):
    print(number, "is an Armstrong number.")
else: print(number, "is not an Armstrong number.")

# Check if the number is a palindrome
if is_palindrome(number):
    print(number, "is a palindrome.")
else: print(number, "is not a palindrome.")


