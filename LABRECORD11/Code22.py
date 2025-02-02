# Write a python program to search an element in a list.
# If the element found, print the position of the element.
# Print an appropriate message if the element is not found.

n=int(input("Enter the number of elements: "))
l=[]
for i in range(n):
    val=int(input("Enter element: "))
    l.append(val)
num=int(input("Enter the elements to be searched: "))
flag=0
for i in range (len(l)):
    if l[i]==num:
        flag=1
        break
    else:
        flag=0
print("The original list in: ", l)
if flag==1:
    print("Element found in position: ", i)
else:
    print("Element not found in the list.")
