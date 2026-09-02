i= int(input("Enter a starting number:\t"))
x= int(input("Enter an ending number:\t"))
c=0
print("Even numbers are:\t")
while(i<=x):
    if i%2==0:
        print(i)
        c+=1
    i+=1
print("The number of even numbers are:-\n")
print(c)
