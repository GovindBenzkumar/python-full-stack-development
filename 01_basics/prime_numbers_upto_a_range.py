x= int(input("Enter the starting range:\n"))
y= int(input("Enter the ending range:\n"))

for i in range(x,y+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i)
            
            
    


