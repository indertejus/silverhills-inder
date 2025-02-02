# Write a python program to display the number of 
# different types of characters in a given string.

data=input("Enter the string: ")
print("Actual data is: ")
print(data)

vowels='aeiouAEIOU'
numvowels=0
consonants=0
small=0
capital=0
numbers=0
special=0

for i in data:
    for j in i:
        if j.isalnum()==False:
            special+=1
        if j.isdigit()==True:
            numbers+=1
        if j in vowels:
            numvowels+=1
        if j.isupper()==True:
            capital+=1
        if j.islower()==True:
            small+=1
        if j not in vowels and j.isalpha()==True:
            consonants+=1

print("Lower case: ", small)
print("Upper case: ", capital)
print("Vowels case: ", numvowels)
print("Consonants case: ", consonants)
print("Number case: ", numbers)
print("Special case: ", special)
