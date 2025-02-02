# Write a python program to find largest and smallest
# element in a list.
n=int(input("Enter the number of elements: "))
l=[]
m=0
for i in range(n):
    val=int(input("Enter elements: "))
    l.append(val)
print("The original list is: ", l)
for i in l:
    if i>m:
        m=i
print("Largest number: ", m)
for i in l:
    if i<m:
        m=i
print("Smallest number: ", m)