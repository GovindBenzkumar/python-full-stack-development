import mysql.connector
con=mysql.connector.connect(user="root",password="134340",host="localhost",database="base")
con.autocommit=True
cur=con.cursor()

#cur.execute("create database base")
cur.execute("create table if not exists admin(user_name varchar(30), password varchar(30)")
cur.execute("insert into admin values('admin123','134340')")
#cur.execute("create table if not exists category(c_id int auto_increment primary key,c_name varchar(100),description text)")
#cur.execute("create table if not exists branch(b_id int auto_increment primary key,b_name varchar(100),address text,district varchar(100),phone varchar(100),email varchar(100),password varchar(100))")
#cur.execute("create table if not exists parcel(p_id int auto_increment primary key,c_id int,source_b_id int,destination_b_id int,sender_name varchar(100),sender_phone varchar(100),sender_address text,receiver_name varchar(100),receiver_phone varchar(100),receiver_address text,weight decimal(8,2),booking_date datetime,delivery_date datetime,delivery_charge decimal(10,2),payment_status varchar(20),parcel_status varchar(30))")

def admin_login():
    u = input("Enter the username")
    p = input("Enter the password")
    cur.execute("select * from admin where user_name= %s and password= %s", (u,p))
    d=cur.fetchone()
    if d:
        print("Login successful")
        adminmenu()
    else:
        print("Incorrect Username or Password")
def register_category():
    i=int(input("Enter the limit"))
    for i in range(1,i+1):
        c_name=input("Enter the category name")
        desc=input("Enter the category description")
        cur.execute("insert into category(c_name,description) values (%s,%s)",(c_name,desc))
def view_category():
    cur.execute("select * from category")
    d=cur.fetchall()
    for i in d:
        print("Category Id : ",i[0])
        print("Category Name : ",i[1])
        print("Category Description : ",i[2])
def register_branch():
    i=int(input("Enter the limit"))
    for i in range(1,i+1):
        b_name=input("Enter the branch name")
        address=input("Enter the branch address")
        district=input("Enter the branch district")
        phone=input("Enter the branch phone")
        email=input("Enter the branch email")
        password=input("Enter the branch password")
        cur.execute("insert into branch(b_name,address,district,phone,email,password) values(%s,%s,%s,%s,%s,%s)",(b_name,address,district,phone,email,password))


def manage_branch():
    print("choice 1: Update\nchoice 2: Delete")
    choice=int(input("Enter your choice"))
    if choice==1:
        b_name=input("Enter the branch name")
        email=input("Enter the branch email")
        cur.execute("update branch set b_name=%s where email=%s",(b_name,email))
    elif choice==2:
        branch_id=int(input("Enter the branch id"))
        cur.execute("delete from branch where branch_id= %s", (branch_id,))
    else:
        print("incorrect choice")




def view_category_parcel():
    c_name = input("Enter the category name")
    cur.execute("select * from parcel where c_name= %s", (c_name,))
    d=cur.fetchall()
    for i in d:
        print("Parcel Id : ",i[0])
        print("Category Id : ",i[1])
        print("Source branch Id: ",i[2])
        print("Destination branch Id: ",i[3])
        print("Sender name : ",i[4])
        # print("Sender phone : ",i[5])
        print("Sender address : ",i[6])
        print("Receiver name : ",i[7])
        # print("Receiver phone : ",i[8])
        print("Receiver address : ",i[9])
        # print("Weight : ",i[10])
        print("Booking date : ",i[11])
        print("Delivery date : ",i[12])
        print("Delivery charge : ",i[13])
        print("Payment status : ",i[14])
        print("Parcel status : ",i[15])

def view_delivered_nondelivered_parcel():
    print("choice 1: Delivered\nchoice 2: Non_delivered")
    choice=int(input("Enter your choice"))
    if choice==1:
        cur.execute("select * from parcel where parcel_status = 0")
        d=cur.fetchall()
        for i in d:
            print("Parcel Id : ", i[0])
            print("Category Id : ", i[1])
            print("Source branch Id: ", i[2])
            print("Destination branch Id: ", i[3])
            print("Sender name : ", i[4])
            # print("Sender phone : ",i[5])
            print("Sender address : ", i[6])
            print("Receiver name : ", i[7])
            # print("Receiver phone : ",i[8])
            print("Receiver address : ", i[9])
            # print("Weight : ",i[10])
            print("Booking date : ", i[11])
            print("Delivery date : ", i[12])
            print("Delivery charge : ", i[13])
            print("Payment status : ", i[14])
            print("Parcel status : ", i[15])
    elif choice==2:
        cur.execute("select * from parcel where parcel_status = 1")
        d=cur.fetchall()
        for i in d:
            print("Parcel Id : ", i[0])
            print("Category Id : ", i[1])
            print("Source branch Id: ", i[2])
            print("Destination branch Id: ", i[3])
            print("Sender name : ", i[4])
            # print("Sender phone : ",i[5])
            print("Sender address : ", i[6])
            print("Receiver name : ", i[7])
            # print("Receiver phone : ",i[8])
            print("Receiver address : ", i[9])
            # print("Weight : ",i[10])
            print("Booking date : ", i[11])
            print("Delivery date : ", i[12])
            print("Delivery charge : ", i[13])
            print("Payment status : ", i[14])
            print("Parcel status : ", i[15])
    else:
        print("invalid choice")

def adminmenu():
    while True:
        print("choice1=Register category\nchoice2=View category\nchoice3=Register branch\nchoice4=Manage branch\nchoice5=View category parcel\nchoice6=View delivered or none delivered parcel")
        choice = int(input("Enter your choice"))
        if choice == 1:
            register_category()
        elif choice == 2:
            view_category()
        elif choice == 3:
            register_branch()
        elif choice == 4:
            manage_branch()
        elif choice == 5:
            view_category_parcel()
        elif choice == 6:
            view_delivered_nondelivered_parcel()
        else:
            print("invalide choice")
            break


def manager_login():
    e = input("Enter the branch email ")
    p = input("Enter the password")
    cur.execute("select * from branch where email= %s and password= %s", (e,p))
    d = cur.fetchone()
    if d:
        print("Login successful")
        managermeanu()
    else:
        print("Incorrect Username or Password")


def parcel_booking():
    i=int(input("Enter the number of parcels"))
    for i in range (1,i+1):
        c_id=int(input("Enter the category id"))
        s_b_id=int(input("Enter the source branch id"))
        d_b_id=int(input("Enter the destination branch id"))
        s_name=input("Enter the sender name")
        s_phone=input("Enter the sender phone")
        s_address=input("Enter the sender address")
        r_name=input("Enter the receiver name")
        r_phone=input("Enter the receiver phone")
        r_address=input("Enter the receiver address")
        weight=float(input("Enter the weight"))
        b_date=input("Enter the booking date")
        d_date=input("Enter the delivery date")
        d_charge=float(input("Enter the delivery charge"))
        pay_status=input("Enter the payment status")
        p_status="1"
        cur.execute("""insert into parcel(p_id ,c_id ,source_b_id ,destination_b_id ,sender_name ,
        sender_phone ,sender_address ,receiver_name ,receiver_phone 
        ,receiver_address ,weight ,booking_date ,delivery_date ,delivery_charge ,
        payment_status ,parcel_status)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
(c_id,s_b_id,d_b_id,s_name,s_phone,s_address,r_name,r_phone,r_address,weight,b_date,d_date,d_charge,pay_status,p_status))

def view_parcel_booking():
    cur.execute("select * from parcel")
    d=cur.fetchall()
    for i in d:
        print("Parcel Id : ", i[0])
        print("Category Id : ", i[1])
        print("Source branch Id : ", i[2])
        print("Destination branch Id : ", i[3])
        print("Sender name : ", i[4])
        print("Sender phone : ", i[5])
        print("Sender address : ", i[6])
        print("Receiver name : ", i[6])
        print("Receiver phone : ", i[7])
        print("Receiver address : ", i[8])
        print("Weight : ", i[9])
        print("Booking date : ", i[10])
        print("Delivery date : ", i[11])
        print("Payment status : ", i[12])
        print("Parcel status : ", i[13])


def view_branch_delivered_parcels():
    b_id = int(input("Enter the branch id: "))

    cur.execute("select * from parcel where destination_b_id = %s and parcel_status = %s", (b_id, 0))

    d = cur.fetchall()

    if d:
        for i in d:
            print("\nParcel Id:", i[0])
            print("Category Id:", i[1])
            print("Source Branch Id:", i[2])
            print("Destination Branch Id:", i[3])
            print("Sender Name:", i[4])
            print("Sender Phone:", i[5])
            print("Sender Address:", i[6])
            print("Receiver Name:", i[7])
            print("Receiver Phone:", i[8])
            print("Receiver Address:", i[9])
            print("Weight:", i[10])
            print("Booking Date:", i[11])
            print("Delivery Date:", i[12])
            print("Delivery Charge:", i[13])
            print("Payment Status:", i[14])
            print("Parcel Status:", i[15])
    else:
        print("No delivered parcels found for this branch.")


def update_parcel():
    p_id=int(input("Enter the parcel id"))
    print("choice 1: Delivered\nchoice 2: Non_delivered")
    choice=int(input("Enter your choice"))
    if choice==1:
        cur.execute("update parcel set parcel_status = 0 where parcel_status = 1 and p_id = %s", (p_id))
    elif choice==2:
        cur.execute("update parcel set parcel_status = 1 where parcel_status = 0 and p_id = %s", (p_id))
    else:
        print("invalide choice")


def managermeanu():
    while True:
        print("choice1=Parcel booking\nchoice2=View parcel booking\nchoice3=View branch delivered parcels\nchoice4=Update parcel")
        choice = int(input("Enter your choice"))
        if choice == 1:
            parcel_booking()
        elif choice == 2:
            view_parcel_booking()
        elif choice == 3:
            view_branch_delivered_parcels()
        elif choice == 4:
            update_parcel()
        else:
            print("invalide choice")
            break


while True:
    print("choice1=Admin login\nchoice2=Manager login")
    choice = int(input("Enter your choice"))
    if choice == 1:
        admin_login()
    elif choice == 2:
        manager_login()
    else:
        print("Invalid choice")
        break


