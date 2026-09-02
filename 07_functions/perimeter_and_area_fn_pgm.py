def rectangle():
    while True:
        print("\n1.Perimeter\n2.Area\n3.Exit\n")
        ch= int(input("Enter your choice:\n"))
        if ch==1:
            l= int(input("Enter the length of rectangle\n"))
            b= int(input("Enter the breadth of rectangle\n"))
            perimeter= 2*(l+b)
            print("Perimeter of rectangle is",perimeter)
        elif ch==2:
            l= int(input("Enter the length of rectangle\n"))
            b= int(input("Enter the breadth of rectangle\n"))
            area= l*b
            print("Area of rectangle is",area)
        elif ch==3:
            break
        else:
            print("Invalid input")

            
def square():
    while True:
        print("\n1.Perimeter\n2.Area\n3.Exit\n")
        ch= int(input("Enter your choice:\n"))
        if ch==1:
            s= int(input("Enter the side of square\n"))
            perimeter= 4*s
            print("Perimeter of square is",perimeter)
        elif ch==2:
            s= int(input("Enter the side of square\n"))
            area= s*s
            print("Area of square is",area)
        elif ch==3:
            break
        else:
            print("Invalid input")


def circle():
    while True:
        print("\n1.Perimeter\n2.Area\n3.Exit\n")
        ch= int(input("Enter your choice:\n"))
        if ch==1:
            r= int(input("Enter the radius of circle\n"))
            perimeter= 2*3.14*r
            print("Perimeter of circle is",perimeter)
        elif ch==2:
            r=int(input("Enter the radius of circle\n"))
            area= 3.14*r*r
            print("Area of circle is",area)
        elif ch==3:
            break
        else:
            print("Invalid input")

while True:
    print("\nMain Menu\n\n1.Rectangle\n2.Square\n3.Circle\n4.Exit")
    choice=int(input("Enter your choice:\n"))
    if choice==1:
        rectangle()
    elif choice==2:
        square()
    elif choice==3:
        circle()
    elif choice==4:
        print("The program got exited")
        break
    else:
        print("Invalid input")

        
    
           
            
  
