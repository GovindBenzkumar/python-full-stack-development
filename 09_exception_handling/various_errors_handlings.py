'''try:
    l= [1,2,3,4]
    print(l[2])

except IndexError:
    print("IndexError:Please enter a valid index range")

else:
    print("No error")
finally:
    print("Thank you")

try:
    d= {1:"apple",2:"banana",3:"mango",4:"orange"}
    print(d[10])
except KeyError:
    print("KeyError:Enter a valid key")

try:
    import os
except ModuleNorFoundError:
    print("ModuleNotFoundError:- Please import a valid module")
else:
    print("This is a valid module")

try:
    f= open("aliens.txt","x")
except FileExistsError:
    print("FileExistsError:- File already exists")
else:
    print("File got created")'''

try:
    f= open("aliens.txt","r")
except FileNotFoundError:
    print("File does not exist")
else:
    print("File exists in the directory")










