print("Welcome to Failure Calculator")
m1=int(input("Enter your English:"))
m2=int(input("Enter your Computer Science:"))
m3=int(input("Enter your Physics:"))
m4=int(input("Enter your Chemistry:"))
m5=int(input("Enter your Biology:"))

totalmark=500
actualmark=m1+m2+m3+m4+m5

percent=actualmark/totalmark * 100
print("Your % is :", percent)
if percent>=90:
    print("Ok very good, A1")
elif percent>=80 and percent<90:
    print("Almost escaped the slipper, A2")
else:
    print("YOU DAMNED EMOTIONAL DAMAGE")
    print("GET OUT")
