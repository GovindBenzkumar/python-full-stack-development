f= open("m1.txt","w")
x= int(input("enter the starting number"))
y= int(input("enter the ending number"))
for i in range(x,y+1):
    for j in range(1,11):
        p=str(i)+ "*"+ str(j)+ "="+str(i*j)
        f.write(p+"\n")
f.close()