x = int(input("Enter the number:\n"))
sum= 0
for i in range(1,x):
    if x%i== 0:
        sum=sum+i
        print(i)
if sum==x:
    print("This is a perfect number")
else:
    print("The number is not perfect")

        
