print("Welcome to Failure Calculator \nThis is where you can calculate your marks! \nBeware: If your mark is below 50% (C Grade), you're getting the Slipper™ \n\nMarks are out of 100")
enm=int(input("\nEnter your English:"))
csm=int(input("\nEnter your Computer Science:"))
phm=int(input("\nEnter your Physics:"))
chm=int(input("\nEnter your Chemistry:"))
bim=int(input("\nEnter your Biology:"))


tm=500
am=enm+csm+phm+chm+bim

pct=am/tm * 100
print("Your % is :", pct, "\n")

if enm>60:
    if enm>=80:
        print("Good, you have A1 in English")
    elif enm>=80:
        print("You have A2 in English")
    elif enm>=70:
        print("You have a B1 in English, bruh™")
    else enm<70:
        print("FAILURE")

if csm>60:
    if csm>=80:
        print("Good, you have A1 in English")
    elif csm>=80:
        print("You have A2 in English")
    elif csm>=70:
        print("You have a B1 in English, bruh™")
    else:
        print("FAILURE")

if phm>60:
    if phm>=90:
        print("Good, you have A1 in Physics")
    elif phm>=80:
        print("You have A2 in Physics")
    elif phm>=70:
        print("You have a B1 in Physics, bruh™")
    else:
        print("FAILURE")

if chm>60:
    if chm>=90:
        print("Good, you have A1 in Chemistry")
    elif chm>=80:
        print("You have A2 in Chemistry")
    elif chm>=70:
        print("You have a B1 in Chemistry, bruh™")
    else:
        print("FAILURE")

if bim>60:
    if bim>=90:
        print("Good, you have A1 in Biology")
    elif bim>=80:
        print("You have A2 in Biology")
    elif bim>=70:
        print("You have a B1 in Biology, bruh™")
    else:
        print("FAILURE")
