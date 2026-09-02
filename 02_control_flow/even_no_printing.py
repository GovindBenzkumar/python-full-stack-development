x= int(input("Enter the starting value:\n"))
y= int(input("Enter the ending value:\n"))
count=0
print("Even numbers from this list are:\n")
for i in range(x,y+1):
    if i%2==0:
        print(i)
        count+=1
print("Number of even numbers:-",count)
        
