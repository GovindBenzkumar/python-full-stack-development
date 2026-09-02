import os
#os.remove('m3.txt')
if os.path.exists("new.txt"):
    print("File exists")
else:
    print("File doesn't exist")
    open("new.txt",'x')

