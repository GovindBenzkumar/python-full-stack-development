def Rectangle():
    l= int(input("Enter the length of rectangle:\n"))
    b= int(input("Enter the breadth of rectangle:\n"))
    area= l*b
    print("Area of rectangle is",area)

def Square():
    s= int(input("Enter the side of square:\n"))
    area= s*s
    print("Area of square is",area)

def circle():
    r= int(input("Enter the radius of circle:\n"))
    area= 3.14*r*r
    print("Area of circle is",area)

while True:
    print("1.Rectangle\n2.Square\n3.Circle\n4.Exit")
    choice= int(input("Enter your choice:\n"))
    if choice==1:
        Rectangle()
    elif choice==2:
        Square()
    elif choice==3:
        circle()
    elif choice==4:
        print("The program got exited!")
        break
    else:
        print("Invalid input")
    
    
            
            

