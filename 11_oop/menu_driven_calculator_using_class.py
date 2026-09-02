class calculator:
    def add(self):
        a= int(input("Enter a number"))
        b= int(input("Enter another number"))
        print(a+b)
    def sub(self):
        a = int(input("Enter a number"))
        b = int(input("Enter another number"))
        print(a-b)
    def prod(self):
        a = int(input("Enter a number"))
        b = int(input("Enter another number"))
        print(a*b)
    def div(self):
        a = int(input("Enter a number"))
        b = int(input("Enter another number"))
        print(a/b)

s= calculator()
while True:
    print("Calculator\n 1.Add\n 2.Sub\n 3.Prod\n 4.Div\n 5.Exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        s.add()
    elif choice == 2:
        s.sub()
    elif choice == 3:
        s.prod()
    elif choice==4:
        s.div()
    elif choice==5:
        print("Thanks for using this program")
        break
    else:
        print("Please enter a valid choice")







