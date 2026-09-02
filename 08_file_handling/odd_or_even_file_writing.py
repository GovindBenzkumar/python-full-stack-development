f= open("m1.txt","w")
g= open("m2.txt","w")
for i in range(1,11):
    if i % 2 == 0:
        f.write(str(i) + "\n")
    else:
        g.write(str(i) + "\n")
