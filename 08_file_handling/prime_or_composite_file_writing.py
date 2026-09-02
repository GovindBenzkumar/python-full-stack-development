f= open("m2.txt","w")
x= int(input("Enter the starting number"))
y= int(input("Enter the ending number"))
for i in range(x,y+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        f.write(str(i)+"\n")
