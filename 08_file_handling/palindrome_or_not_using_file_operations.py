f= open("file.txt",'r')
g= open("m2.txt","w")
l= f.readlines()
print(l)
for i in l:
    k= i.strip("\n")
    s=""
    for j in k:
        s=j+s
    if s==k:
        g.write(i)
    else:
        print(i,"is not palindrome")
f.close()