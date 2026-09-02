a= int(input("Enter 1st number:\t"))
b= int(input("Enter 2nd number:\t"))
c= int(input("Enter 3rd number:\t"))
d= int(input("Enter 4th number:\t"))
if a>b and a>c and a>d:
    print(a,"is greatest")
elif b>a and b>c and b>d:
    print(b,"is greatest")
elif c>a and c>b and c>d:
    print(c,"is greatest")
elif d>a and d>b and d>c:
    print(d,"is greatest")
else:
    print("All numbers are equal")
