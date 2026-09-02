x= int(input("Enter a number:\t"))
i=1
c=0
print("Factors are:\t")
while(i<=x):
    if x%i==0:
        print(i)
        c+=1
    i+=1
    
print("The number of factors are:-\n")
print(c)
    
        
        
