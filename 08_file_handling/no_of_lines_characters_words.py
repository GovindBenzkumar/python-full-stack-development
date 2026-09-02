f= open('file.txt','r')
count=0
x= f.readlines()
for i in x:
    for j in i:
        print(j)
f.close()