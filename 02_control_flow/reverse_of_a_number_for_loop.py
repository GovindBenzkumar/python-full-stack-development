x= int(input("Enter a number:\n"))
rev= 0
for i in range(0,x):
    i= x%10
    rev= rev*10+i
    x= x//10
print(rev)
