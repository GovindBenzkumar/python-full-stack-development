a= int(input("Enter the 1st number: "))
b= int(input("Enter the 2nd number: "))
c= int(input("Enter the 3rd number: "))
if a>b and a>c:
    n=a
    print(a,"is greatest")
elif b>a and b>c:
    n=b
    print(b,"is greatest")
elif c>a and c>b:
    n=c
    print(c,"is greatest")
else:
    n=a=b=c
    print("All numbers are equal")

if n%2==0:
    print(n,"is even number")
else:
    print(n,"is odd number")

