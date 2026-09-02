list=[1,2,3,4,5,6,7,8,9]
for i in range(len(list)):
    for j in range(i):
        s= list[i]+list[j]
        if s==10:
            print(list[i], list[j])
