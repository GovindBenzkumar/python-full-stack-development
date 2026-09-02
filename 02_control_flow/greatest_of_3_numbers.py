x= int(input("Enter 1st number:\t"))
y= int(input("Enter 2nd number:\t"))
z= int(input("Enter 3rd number:\t"))
if x>y and x>z:
    print(x,"is greatest")
elif y>x and y>z:
    print(y,"is greatest")
elif z>x and z>y:
    print(z,"is greatest")
else:
    print("All numbers are equal")
