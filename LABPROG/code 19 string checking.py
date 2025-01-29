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
        
