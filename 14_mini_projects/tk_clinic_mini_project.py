from tkinter import *
import mysql.connector
con = mysql.connector.connect(user="root", password= "134340", host="localhost", database="clinic")
con.autocommit=True
cur=con.cursor()
#cur.execute("create database clinic")
#cur.execute("create table if not exists admin(admin_id int auto_increment primary key,username varchar(30) unique,password varchar(30))")
#cur.execute("insert into admin values('admin123','134340')")
#cur.execute("create table if not exists user(user_id int auto_increment primary key,name text,age text,gender text,phone int, address text, username varchar(30) unique, password varchar(30))")
#cur.execute("create table if not exists medical_test(test_id int,test_name text,description text,price float)")
#cur.execute("create table if not exists test_booking(booking_id int auto_increment primary key,user_id int,test_id int,booking_date int,status text,result text,payment_status text)")

sample=Tk()
sample.geometry("600x600")
sample.configure(bg="pink")
sample.title("welcome")
Label(sample,text= "CLINIC SOFTWARE",bg="pink",fg="red",font=("Times New Roman", 30, "bold")).place(x=130,y=50)
def admin_login():
    adm = Toplevel(sample)
    adm.geometry("400x500")
    adm.title("admin login")
    adm.configure(bg="pink")
    Label(sample)

def user_login():
    adm = Toplevel(sample)
    adm.geometry("400x500")
    adm.title("user login")
    adm.configure(bg="pink")

btn=Button(sample,text="Admin",font=("Times New Roman", 20, "bold"),command=admin_login)
btn.place(x=300,y=200)
btn=Button(sample,text="User",font=("Times New Roman", 20, "bold"),command=user_login)
btn.place(x=300,y=300)

sample.mainloop()
