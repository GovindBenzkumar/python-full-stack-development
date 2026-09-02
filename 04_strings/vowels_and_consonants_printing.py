x= input("Enter a string:\n")
index= 0
count_v=0
count_c=0
vowels= "aeiou"
while index < len(x):
    if x[index] in vowels:
        print("vowels are:\n",x[index])
        count_v+=1
    else:
        print("consonants are:\n",x[index])
        count_c+=1
    index+=1
print("Number of vowels:\n",count_v)
print("Number of consonants:\n",count_c)
        
