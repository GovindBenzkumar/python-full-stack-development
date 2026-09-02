l= [1,2,3,4,5,6]
def search(n):
    return n%2==0
k= filter(search,l)
print(list(k))


