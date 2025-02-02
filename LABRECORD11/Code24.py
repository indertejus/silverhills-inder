# Write a python program to create a dictionary of student,
# name and mark.
# Find the student name who secured maximum mark.

num= int(input("Enter the number of students to be added: "))
name1={}
max=0
for i in range(num):
    key=input("Enter the name of student: ")
    value=int(input("Enter the mark: "))
    name1[key]=value
print("The dictionary: ")
print(name1)
for i in name1:
    if(name1[i]>max):
        max=name1[i]
        max_name=i
print("The student who secured maximum mark is: ", max_name)
