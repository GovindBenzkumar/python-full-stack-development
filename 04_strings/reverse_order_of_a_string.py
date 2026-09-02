x= input("Enter a string:\n")
rev= ''
index= 0
while index < len(x):
    rev= x[index] + rev
    index += 1
print(rev)
    
