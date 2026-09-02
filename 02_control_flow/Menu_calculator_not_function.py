while True:
    a= int(input("Enter the first number:\n"))
    b= int(input("Enter the second number:\n"))
    operator= input("Enter the operator(+,-,*,/):\n")
    if operator=="+":
        print("Sum is",a+b)
    elif operator=="-":
        print("Difference is",a-b)
    elif operator=="*":
        print("Product is",a*b)
    elif operator=="/":
        print("Division is",a/b)
