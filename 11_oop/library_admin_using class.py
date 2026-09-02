class library:
    def add_book(self):
        self.id= int(input("Enter book id"))
        self.name= input("Enter book title")
        self.price= int(input("Enter book price"))

    def display_book(self):
        print("Book ID:- ",self.id)
        print("Book Name:- ",self.name)
        print("Book Price:- ",self.price)

    def search_book(self):
        b_id= int(input("Enter the book id of the book you want to search"))

    def update_price(self):
        b_id= int(input("Enter the book id of the book you want to update"))

    def delete_book(self):
        b_id= int(input("Enter the book id of the book you want to delete"))

l=[]

while True:
    print(" Welcome to the library Admin Page ")
    print("1.Add Book\n2.Display Book\n3.Search Book\n4.Update Book\n5.Delete Book\n6.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        book= library()
        book.add_book()
        l.append(book)

    elif choice==2:
        for i in l:
            i.display_book()

    elif choice==3:
        b_id= int(input("Enter the book id of the book you want to search"))
        for i in l:
            if i.id==b_id:
                i.display_book()
            else:
                print("")

    elif choice==4:
        b_id= int(input("Enter the book id of the book you want to update"))
        for i in l:
            if i.id== b_id:
                i.price= int(input("Enter the updated book price"))
                print("Price got updated")
            else:
                print("Book/ Book ID not found")

    elif choice==5:
        b_id= int(input("Enter the book id of the book you want to delete"))
        for i in l:
            if i.id== b_id:
                l.remove(i)
                print("Book got deleted")
            else:
                print("Book/ Book ID not found")

    elif choice==6:
        print("Thank you for using this program")
        break

    else:
        print("Please enter a valid choice")

















