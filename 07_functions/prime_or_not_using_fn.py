def prime_or_not():
    num= int(input("Enter the number:\n"))
    count=0
    i=1
    while(i<=num):
        if(num%i==0):
            count+=1
        i+=1
    if count==2:
        print("It is a prime number")
    else:
        print("It is a composite number")

prime_or_not()
    
