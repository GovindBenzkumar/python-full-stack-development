x= int(input("Enter 1st number:\t"))
y= int(input("Enter 2nd number:\t"))
z= int(input("Enter 3rd number:\t"))
if x<y and x<z: 
    print(x,"is smallest")
    p=x
elif y<x and y<z:
    print(y,"is smallest")
    p=x
elif z<x and z<y:
    print(z,"is smallest")
    p=x
else:
    print("All numbers are equal")
if p%2==0:
    print("It is an even number")
else:
    print("It is an odd number")
