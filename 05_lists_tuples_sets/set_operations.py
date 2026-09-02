'''s= {'apple','banana','cherry'}
s.add('orange')
s.clear()
print(s)
copy_set= s.copy()
copy_set.add('mango')
print(s)
print(copy_set)
t= {'apple','mango','grapes'}
b= s.difference(t)
print(b)'''

''''x= {'apple','orange','banana'}
y={'cherry','papaya','apple'}
x.difference_update(y)
print(x)'''

'''s={'apple','orange','banana'}
s.discard('apple')
print(s)'''

'''s={'apple','orange','banana'}
s.remove('apple')
print(s)'''

'''x= {'apple','orange','banana'}
y= {'cherry','papaya','apple'}
z= x.intersection(y)
print(z)'''

x= {'apple','orange','banana'}
y= {'cherry','papaya','apple'}
x.intersection_update(y)
print(x)

'''x= {'apple','orange','banana'}
y= {'cherry','papaya'}
z= x.isdisjoint(y)
print(z)'''

'''s1= {'apple',23,24}
s2= {'orange',23,27}
s1.update(s2)
print(s1)'''







