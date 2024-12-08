list1 = list(input("Enter something:"))
confirm = int(input("Do you want to print the list? Yes(1)/No(0)"))
yes = 1
no = 0
if confirm == yes:
    print(list1)
elif confirm == no:
    print("Exiting...")
else: print("What the hell bro?")
