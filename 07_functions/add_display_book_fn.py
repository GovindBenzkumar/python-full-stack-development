l=[]
def add_book():
    ID= int(input("Enter the unique Book ID:-\n"))
    name= input("Enter the name of book:-\n")
    price= float(input("Enter the price of book:-\n"))
    qty= int(input("Enter the number of books you are adding:\n"))
    l.append([ID,name,price,qty])

def display_book():
    for i in l:
        print("ID=",i[0])
        print("Name:",i[1])
        print("Price:",i[2])
        print("No. of books:",i[3])

def search():
    ID= int(input("Enter the ID of book to search\n"))
    for i in l:
        if i[0]==ID:
            print("id=",i[0])
            print("name=",i[1])
            print("price=",i[2])
            print("No. of books=",i[3])

def update():
    ID= int(input("Enter the id"))
    price= int(input("enter the price"))
    for i in l:
        if i[0]==ID:
            i[2]= price
            print("id=",i[0])
            print("name=",i[1])
            print("price=",i[2])
            print("quantity=",i[3])

def delete():
    id= int(input("Enter the ID"))
    for i in l:
        if i[0]== id:
            l.remove(i)
            print("removed")


while True:
    print("Main Menu\n\n1.Add Book\n2.Display Book\n3.Search\n4.Update\n5.Delete\n6.Exit")
    choice= int(input("Enter your choice\n\n"))
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
        print("Program got exited!\n")
        break
    else:
        print("Please enter valid input\n")
        
    

    
                 
