x= input("Enter a string:\t")
index=0
count=0
while index < len(x):
    if x[index] in "aeiou":
        print(x[index])
        count+=1
    index+=1
print("Number of vowels in",x,"is",count)
    
