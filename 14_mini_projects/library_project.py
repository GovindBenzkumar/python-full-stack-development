books=[]
def add_book():
    b_id= int(input("Enter the unique Book ID:-\n"))
    name= input("Enter the name of book:-\n")
    price= float(input("Enter the price of book:-\n"))
    qty= int(input("Enter the number of books you are adding:\n"))
    l.append([b_id,name,price,qty])

def display_book():
    for i in books:
        print("id=",i[0])
        print("name=",i[1])
        print("price=",i[2])
        print("quantity=",i[3])

def search():
    b_id= int(input("Enter the ID:-"))
    for i in books:
        if i[0]==id:
            print("ID=",i[0])
            print("Name=",i[1])
            print("Price=",i[2])
            print("Quantity=",i[3])

def update():
    b_id= int(input("Enter the book ID:-"))
    price= int(input("Enter the price:-"))
    for i in books:
        if i[0]== b_id:
            i[2]==price
            print("id=",i[0])
            print("name=",i[1])
            print("price=",i[2])
            print("quantity=",i[3])

def delete():
    id= int(input("Enter the id"))
    for i in books:
        if i[0]==id:
            books.remove(i)
            print("removed")
    
        
def admin():
    a_username= input("Enter the Username:-")
    a_password= input("Enter the Password:-")
    if a_username== "admin123" and a_password== "12345xyz":
        print(" Welcome to the Admin Page:-")
        while True:
            print("1.Add Books\n2.Display Books\n3.Search Books\n4.Update Books\n5.Delete Books\n Enter your choice")
            choice= int(input("Enter your choice\n"))
            if choice==1:
                add_book()
            elif choice==2:
                display_book()
            elif choice==3:
                search()
            elif choice==4:
                update()
            elif choice==5:
                delete()
            elif choice==6:
                print("Exited from Admin page")
                break
            else:
                print("invalid choice")

def register():
    print(books)
    username= input("Enter the username:\n")
    password= input("Enter the password:\n")
    name= input("Enter the name:\n")
    ph_no= input("Enter the phone no.\n")
    email= input("Enter the email:")
    books.append([username,password,name,ph_no,email])
    print("Registration successfully")

def login():
    username= input("Enter the username:\n")
    password= input("Enter the password:\n")
    for i in books:
        if i[0]== username:
            i[1]==password
            print("Login successfully")
        else:
            print("User not found")
def user:
    u_register= input("Enter the register")
    u_login= input("Enter the login")
    print("Welcome to User page")
    while True:
        print("1.Register\n2.Login\n3.Exit\n")
        choice= int(input("Enter your choice"))
        if choice==1:
            register()
        elif choice==2:
            login()
        elif choice==3:
            print("Thank you")
            break
        else:
            print("Invalid choice")
while True:
    print("1.Admin\n2.User\n")
    choice=int(input("Enter your choice"))
    if choice==1:
        admin()
    elif choice==2:
        user()
    elif choice==3:
        print("exit")
        break
            
        
