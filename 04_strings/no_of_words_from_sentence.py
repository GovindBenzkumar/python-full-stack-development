sen= input("Enter the sentence: ")
count=0
in_word= False
for i in sen:
    if i!= " ":
        if not in_word:
            count+=1
            in_word= True
    else:
        in_word= False
print("Number of words: ",count)




