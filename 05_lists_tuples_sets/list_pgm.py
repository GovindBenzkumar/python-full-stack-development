l= [4,2.0,7,'apple','orange','FYA',7]
def integer():
    s=0
    i=0
    while i<len(l):
        if type(l[i])==int:
            s=s+l[i]
        i+=1
    print("Sum of integers is",s)

integer()
