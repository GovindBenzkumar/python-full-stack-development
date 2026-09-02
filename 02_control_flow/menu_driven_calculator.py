def addition():
    a= int(input("Enter a number:\n"))
    b= int(input("Enter another number:\n"))
    add= a+b
    print("The sum is:",add)

def subtraction():
    a= int(input("Enter a number:\n"))
    b= int(input("Enter another number:\n"))
    diff= a-b
    print("The difference is",diff)

def multiplication():
    a= int(input("Enter a number:\n"))
    b= int(input("Enter another number:\n"))
    prod= a*b
    print("The product is",prod)

def division():
    a= int(input("Enter a number:\n"))
    b= int(input("Enter another number:\n"))
    quot= a/b
    print("The quotient is:",quot)

def modulus():
    a= int(input("Enter a number:\n"))
    b= int(input("Enter another number:\n"))
    mod= a%b
    print("The modulus is:",mod)
    
while True:
    print(" 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Modulus\n 6.Exit")
    choice= int(input("Enter your choice:\n"))
    if choice==1:
        addition()
    elif choice==2:
        subtraction()
    elif  choice==3:
        multiplication()
    elif choice== 4:
        division()
    elif choice== 5:
        modulus()
    elif choice==6:
        print("Program got Exited")
        break
    else:
        print("ERROR-404")
        

        


