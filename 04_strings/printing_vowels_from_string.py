x= input("Enter a string:\n")
index= 0
vowels= "aeiou"
while index < len(x):
    if x[index] in vowels:
        print(x[index])
    index+=1
