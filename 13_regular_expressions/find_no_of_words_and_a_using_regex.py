import re
x= "I need the whole stadium to jump, put your phone down let's get all the fun"
print(x)

w= re.split(' ',x)
print("No. of words are:- ",len(w))
print(w)

'''a= re.findall('a',x)
print("Letter 'A' in the string are:- ",a)'''

b= re.findall('',x)
print(b)






