import psycopg2

con= psycopg2.connect(user='postgres',password='134340',host='localhost',port='5432',database='inventory')
con.autocommit= True
cur = con.cursor()
#cur.execute("create database inventory")
#cur.execute("create table table1(pro_id int, pro_name text, stock int, price float)")
#cur.execute("create table bills(bill_id SERIAL PRIMARY KEY, pro_id INTEGER, pro_name VARCHAR, quantity INTEGER, price INTEGER,total INTEGER)")
def add_product():
    l=int(input("Enter the number of entries you want to add: "))
    for i in range(l):
        a= int(input("Enter product ID: "))
        b= input("Enter product name: ")
        c= int(input("Enter the number of stock of the product: "))
        d= int(input("Enter the price of the product: "))
        print("--------------------------------------")
        cur.execute("select * from table1 where pro_id= %s",(a,))
        if cur.fetchall():
            print("Product ID already exists!")
        else:
            cur.execute("insert into table1 values(%s,%s,%s,%s)", (a,b,c,d))
            print("Data uploaded successfully!")

def display():
    print("Product Details:")
    cur.execute("select * from table1")
    e= cur.fetchall()
    for i in e:
        print("Product ID:- ",i[0])
        print("Name:- ",i[1])
        print("Stock:- ",i[2])
        print("Price:- Rs ",i[3])
        print("-------------------------")

def search_product():
    n= int(input("Enter Product ID: "))
    cur.execute("select * from table1 where pro_id= %s",(n,))
    l= cur.fetchall()
    for i in l:
        print("Product ID:- ",i[0])
        print("Name:- ",i[1])
        print("Stock:- ",i[2])
        print("Price:- ",i[3])

def update_product():
    a= int(input("Enter Product ID of the product to be updated: "))
    b= input("Enter name of the product to be updated: ")
    c= int(input("Enter the number of stock of the product to be updated: "))
    d= int(input("Enter the price of the product to be updated: "))
    cur.execute("update table1 set pro_name= %s, stock= %s, price= %s where pro_id = %s",(b,c,d,a))
    print("Data updated successfully!")

def purchase_product():
    display()
    while True:
        print("1.Purchase item")
        print("2.Back to main menu")
        ch= int(input("Enter an option from the given menu :) "))
        if ch==1:
            pro_id= int(input("Enter product ID: "))
            qty= int(input("Enter quantity: "))

            cur.execute("select * from table1 where pro_id= %s",(pro_id,))
            product= cur.fetchone()
            if product is None:
                print("Product not found")
            else:
                pro_id,pro_name,stock,price= product
                if qty>stock:
                    print("Not enough stock")
                    print("Available stock: ",stock)
                else:
                    total= price*qty
                    cur.execute("update table1 set stock= stock - %s where pro_id= %s",(qty,pro_id,))
                    cur.execute("insert into bills(pro_id,pro_name,quantity,price,total) values(%s,%s,%s,%s,%s)",(pro_id,pro_name,qty,price,total))
                    con.commit()
                    print("\nBILL")
                    cur.execute("select * from bills where pro_id= %s",(pro_id,))
                    f= cur.fetchall()
                    for i in f:
                            print("Product ID:- ", i[1])
                            print("Item Name:- ", i[2])
                            print("Selected Quantity:- ", i[3])
                            print("Price of item:- Rs ", i[4])
                            print("Total amount:- ", i[5])
                            print("-------------------------")
        elif ch==2:
            break
        else:
            print("invalid choice")

def delete_product():
    n= int(input("Enter Product ID of the item to be deleted: "))
    cur.execute("delete from table1 where pro_id= %s",(n,))
    print("Item got deleted successfully!")

while True:
    print("\n")
    print("------------Inventory Menu-------------")
    print("1. Add product")
    print("2. Display products")
    print("3. Purchase product")
    print("4. Search product")
    print("5. Update product")
    print("6. Delete product")
    print("7. Exit")
    choice= int(input("\nEnter an option from the menu :) "))
    print("------------------------------------------")
    if choice==1:
        add_product()
    elif choice==2:
        display()
    elif choice==3:
        purchase_product()
    elif choice==4:
        search_product()
    elif choice==5:
        update_product()
    elif choice==6:
        delete_product()
    elif choice==7:
        print("Thank you for using the program :)")
        break
    else:
        print("Please enter a valid option :|")








