x= int(input("Enter the starting range:\n"))
y= int(input("Enter the ending range:\n"))

for i in range(x,y+1):
    s=0
    for j in range(1,i):
        if i%j==0:
            s=s+j
    if i==s:
        print(i)
