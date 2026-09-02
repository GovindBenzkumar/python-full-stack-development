x= input("Enter a string:\n")
vowels= "aeiou"
print("Vowels from given string are:\n")
for i in range(0,len(x)):
    if x[i] in vowels:
        print(x[i])
