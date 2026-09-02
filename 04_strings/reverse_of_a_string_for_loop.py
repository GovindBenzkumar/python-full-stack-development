x= input("Enter a string:\n")
rev=''
for i in range(0,len(x)):
    rev= x[i]+rev
print(rev)
