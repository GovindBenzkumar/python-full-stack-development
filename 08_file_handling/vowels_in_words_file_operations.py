f= open('file.txt','r')
l= f.readlines()
vowels=['a','e','i','o','u']
for i in l:
    print("Word:",i.strip())
    print("Vowels:",end="")
    for j in i:
        if j in vowels:
            print(j,end="")
    print()






