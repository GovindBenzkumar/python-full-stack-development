import sqlite3
con= sqlite3.connect("library_db")
#con.execute("create table library1(b_id int,name text,price int,qty int)")

def add_book():
    l= int(input("Enter the number of books you want to enter:-\n"))
    for i in range(l):
        b_id= int(input("Enter the id of the book you want to add:-\n"))
        name= input("Enter the name of the book you want to add:-\n")
        price= int(input("Enter the price of the book you want to add:-\n"))
        qty= int(input("Enter the quantity of the book you want to add:-\n"))
        print("---------------------")
        con.execute("insert into library1 values(?,?,?,?)",(b_id,name,price,qty))
        con.commit()

def display_book():
    print("Books available:-\n")
    d=con.execute("select * from library1")
    for b_id,name,price,qty in d:
        print("Book ID:- ",b_id)
        print("Name:- ",name)
        print("Price:- ",price)
        print("Quantity:- ",qty)
        print("-------------------")

def search_book():
    s= int(input("Enter the book ID to be searched:-\n"))
    d=con.execute("select * from library1 where b_id= ?",(s,))
    for b_id,name,price,qty in d:
        print("Book ID:- ",b_id)
        print("Name:- ",name)
        print("Price:- ",price)
        print("Quantity:- ",qty)

def update_book():
    s= int(input("Enter the book ID to be updated:-\n"))
    p= int(input("Enter the updated price:-\n"))
    q= int(input("Enter the updated quantity:-\n"))
    con.execute("update library1 set price= ?,qty= ? where b_id= ?",(p,q,s))
    con.commit()

def delete_book():
    s= int(input("Enter the book ID to be deleted:-\n"))
    con.execute("delete from library1 where b_id= ?",(s,))
    con.commit()

while True:
    print("LIBRARY ADMIN\n,------------\n 1. Add Book\n 2. Display Book\n 3. Search Book\n 4. Update Book\n 5. Delete Book\n 6. Exit")
    choice = int(input("Enter your choice:- "))
    if choice == 1:
        add_book()
    elif choice == 2:
        display_book()
    elif choice == 3:
        search_book()
    elif choice == 4:
        update_book()
    elif choice == 5:
        delete_book()
    elif choice == 6:
        print("Thank you for using this program")
        break
    else:
        print("Enter a valid choice")


