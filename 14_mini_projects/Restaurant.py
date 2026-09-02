orders={}
menu={1:{"item":"Porotta","price":12,"total_quantity":100},2:{"item":"Chicken 65","price":90,"total_quantity":100},3:{"item":"Chicken Biriyani","price":100,"total_quantity":100}}

def view_menu():
    print("Restaurent Menu\n")
    c=1
    for i in menu:
        print(c,".",menu[i]["item"],"-",menu[i]["price"])
        c+=1
o_id=1

def place_order():
    global o_id
    o = int(input("Place your order(s) by choosing the corresponding ID from the Restaurant menu:-\n"))
    if o in menu:
        qty= int(input("Enter the quantity of selected food item:-\n"))
        menu[o]["total_quantity"]-=qty
        total= menu[o]["price"]*qty
        orders.update({o_id:{"food_id":o,"quantity":qty,"total_amount":total}})
        print("Total price :-",total)
        print("Order Placed successfully\n")
        print("Your order ID:-",o_id) 
        o_id+=1

def cancel_order():
    global o_id
    x= int(input("Are you sure!\n Enter the order ID:-\n"))
    if x in orders:
        orders.pop(x)
        print("Order Cancelled")
    else:
        print("No ORDER ID found!")

def generate_bill():
    x= int(input("Enter the order ID\n"))
    if x in orders:
        print("Item:",menu[x]["item"])
        print("Quantity:",orders[x]["quantity"])
        print("Price:",orders[x]["total_amount"])
    else:
        print("No valid order found")
    
    

while True:
    print("\n Restaurant Management System\n1.Food Item Menu\n2.Place Order\n3.Cancel Order\n4.Generate Bill\n5.Exit")
    ch= int(input("Enter your choice\n"))
    if ch==1:
        view_menu()
    elif ch==2:
        place_order()
    elif ch==3:
        cancel_order()
    elif ch==4:
        generate_bill()
    elif ch==5:
        print("Program exited,Thank you for using our services")
        break
    else:
        print("Please choose the correct option!\n")
    
    

        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        

