# Write a python program to swap the adjacent element in a list.

n=int(input("Enter the number of elements: "))
l=[]
for i in range(n):
    val=int(input("Enter the elements: "))
    l.append(val)
print("The original list is: ", l)
length=len(l)
if length%2==0:
    length=len(l)
    for i in range(0, length, 2):
        l[i], l[i+1]=l[i+1],l[i]
    print("List after swap: ", l)
else:
    length=len(l)
    for i in range (0, length-1, 2):
        l[i], l[i+1]=l[i+1],l[i]
    print("List after swap: ", l)