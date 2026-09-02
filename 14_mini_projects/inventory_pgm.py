products= {}
def add_product():
    pid= int(input("Enter product ID:\n"))
    name= input("Enter the product name:\n")
    stock= int(input("Enter the quantity of product:\n"))
    price= int(input("Enter the price of product:\n"))
    products.update({pid:{"name":name,"stock":stock,"price":price}})

def display_product():
    for i in products:
        print("Product ID=",i)
        print("Name=",products[i]["name"])
        print("Stock=",products[i]["stock"])
        print("Price =",products[i]["price"],"\n")

def search_product():
    pid= int(input("Enter product ID:\n"))
    if pid in products:
        print("name:-",products[pid]["name"])
        print("stock:-",products[pid]["stock"])
        print("price:-",products[pid]["price"])
    else:
        print("No product found!")
    
def update_stock():
    pid= int(input("Enter ID:\n"))
    if pid in products:
        new_stock= int(input("Enter the new stock quantity\n"))
        products[pid]["stock"]= new_stock
        print("Stock updated succesfully\n")
    else:
        print("No product found!")

def delete_product():
    pid= int(input("Enter ID:\n"))
    if pid in products:
        products.pop(pid)
        print("Product deleted successfully!")
    else:
        print("No product found!")

while True:
    print("\nInventory Main Menu:-\n1.Add product\n2.Display product\n3.Search product\n4.Update stock\n5.Delete  product\n6.Exit")
    choice= int(input("Enter your choice\n:-"))
    if choice==1:
        add_product()
    elif choice==2:
        display_product()
    elif choice==3:
        search_product()
    elif choice==4:
        update_stock()
    elif choice==5:
        delete_product()
    elif choice==6:
        print("Program Exited")
        break
    else:
        print("Invalid Input!")
    
    













    
    
        
    
