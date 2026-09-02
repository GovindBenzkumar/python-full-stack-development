x= int(input("Enter a number:\n"))
print("Factors are:-\n")
for i in range(1,x+1):
    if x%i== 0:
        print(i)
