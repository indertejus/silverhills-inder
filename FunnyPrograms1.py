def pause():
    prgmPause = input("\nPress any key to continue...\n")

list1 = list(input("Enter something:"))
confirm = int(input("Do you want to print the list? Yes - 1 / No - 0 : "))
yes = 1
no = 0
if confirm == yes:
    print(list1)
elif confirm == no:
    print("Exiting...")
else: print("What the hell bro?")
pause()

for i in list1:
    print(i)
pause()

list2 = [0,1,2,3,4,5,6,7,8,9,0]
sum = 0
for i in list2:
    sum = sum+i
print("The elements in the list are:", list2)
print("The sum is:", sum)
pause()

for kek in list1:
    print(kek)
print("\n", list1[-1],list1[5], list1[-3],list1[0])
pause()

list3=list[1:5]
pause()