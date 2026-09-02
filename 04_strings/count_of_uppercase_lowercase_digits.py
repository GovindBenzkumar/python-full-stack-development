f= open("file.txt","r")
p=f.read()
upper=0
lower=0
for i in p:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
f.close()
print("No. of uppercase letters: ",upper)
print("No. of lowercase letters: ",lower)
