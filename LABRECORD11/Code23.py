# Write a python program to create a tuple of n numbers
# and search an element in a tuple
# If the element found, print the position of the element.
# Print a appropriate message if the element is not found.

t=tuple()
n=int(input("Enter the no. of elements: "))
i=1
while (i<=n):
    a=int(input("Enter the number: "))
    t=t+(a,)
    i+=1
print("Tuple created as: ")
print(t)
num=int(input("Enter the element to be searched: "))
for i in range (n):
    if t[i]==num:
        flag=True
        break
    else:
        flag=False
print("The original list in: ", t)
if (flag==True):
    print("Element found in position: ", i)
else:
    print("Element not found in the list.")
