import re
x= "Hello welcome to my page"
a= re.findall('e',x)
print(a)

b= re.search('welcome',x)
if b:
    print("The string have been found")
else:
    print("The string have not been found")

c= re.sub('page','class',x)
print(c)

d= re.split(' ',x)
print(d)
