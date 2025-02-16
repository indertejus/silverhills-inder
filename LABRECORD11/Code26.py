# Write a python program to create a dictionary to store student name
# and percentage of marks. Then find out the names of students who 
# have secured more than 75% marks
n = int(input("Enter the number of students: "))
result = {}

for i in range(n):
    print("Enter the details of student", i+1)
    name = input("Name of the student: ")
    rno = int(input("Roll number: "))
    eng = int(input("Enter English marks: "))
    math = int(input("Enter Math marks: "))
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    tot = eng + math + phy + chem
    per = (tot / 400) * 100
    result[rno] = [name, per]

print("Student details: ", result)
print("Following students secured more than 75% marks")
for s in result:
    if result[s][1] > 75:
        print(result[s][0])
