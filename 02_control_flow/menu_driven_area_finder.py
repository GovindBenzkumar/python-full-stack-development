class area_finder:
    def rectangle(self):
        a=int(input("Enter the length of the rectangle"))
        b=int(input("Enter the width of the rectangle"))
        print(a*b)
    def square(self):
        a=int(input("Enter the length of the square"))
        print(a*a)
    def circle(self):
        a=int(input("Enter the radius of the circle"))
        print(3.14*a*a)

x= area_finder()
while True:
    print(" Area Finder\n1.Rectangle\n2.Square\n3.Circle\n4.Exit")
    choice=int(input("Enter your choice"))
    if choice==1:
        x.rectangle()
    elif choice==2:
        x.square()
    elif choice==3:
        x.circle()
    elif choice==4:
        print("Thank you for using this program")
        break
    else:
        print("Invalid Choice,Please enter a valid input")
