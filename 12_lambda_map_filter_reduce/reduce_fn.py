l=[1,2,3,4,5]
from functools import reduce
'''def add(a,b):
    return a+b'''
f= reduce(add,l)
print(f)
