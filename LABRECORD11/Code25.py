# Write a program to create a dictionary to store the student
# name and marks seperately.
# Then find the total mark and average

name=input("Enter the name of the student: ")
name1={}
name1['st_name']=name
eng=int(input("English mark: "))
sci=int(input("Science mark: "))
comp=int(input("Computer Science mark: "))
math=int(input("Maths mark: "))
marks={"English":eng, "Maths":math, "Science":sci, "Computer Science":comp}
sum=0

for ky in marks:
    sum=sum+marks[ky]
avg=sum/4
print("Name of the student: ", name1['st_name'])
print("Total marks: ", sum)
print("Average marks: ", avg)

