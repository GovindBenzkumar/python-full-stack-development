l= [4,2,6,8,10,11]
def prime_or_not():
    for i in l:
        c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i)

prime_or_not()
