import sqlite3
con = sqlite3.connect('employee_db')
#con.execute("create table employee1(emp_no int, name text, place text,designation text,mob_no text)")

def add_employee():
    l = int(input("Enter the number of entries you want to enter:"))
    for i in range(l):
        a = int(input("Enter employee ID: "))
        b = input("Enter name: ")
        c = input("Enter place: ")
        d = input("Enter designation: ")
        e = input("Enter mobile no: ")
        print("---------------------")
        con.execute("insert into employee1 values(?,?,?,?,?)", (a, b, c, d, e))
        con.commit()

def display_employee():
    print("Employee Details:- ")
    d=con.execute("select * from employee1")
    for emp_no,name,place,designation,mob_no in d:
        print("employee ID:-",emp_no)
        print("Name:-",name)
        print("Place:-",place)
        print("Designation:-",designation)
        print("Contact no:-",mob_no)
        print("---------------------")

def search_employee():
    e= int(input("Enter the employee ID:- "))
    d=con.execute("select * from employee1 where emp_no=?",(e,))
    for emp_id,name,place,designation,mob_no in d:
        print("employee ID:-",e)
        print("Name:-",name)
        print("Place:-",place)
        print("Designation:-",designation)
        print("Contact no:-",mob_no)

def update_employee():
    f= int(input("Enter the employee ID to be updated:- "))
    a= input("Enter place: ")
    b= input("Enter designation: ")
    c= input("Enter mobile no: ")
    con.execute("update employee1 set place=?,designation=?,mob_no=? where emp_no=?",(a,b,c,f))
    con.commit()

def delete_employee():
    e= int(input("Enter the employee ID to be deleted:- "))
    con.execute("delete from employee1 where emp_no=?",(e,))
    con.commit()

while True:
    print("EMPLOYEE DETAILS\n,------------\n 1. Add employee\n 2. Display employee\n 3. Search employee\n 4. Update employee\n 5. Delete employee\n 6. Exit")
    choice = int(input("Enter your choice:- "))
    if choice == 1:
        add_employee()
    elif choice == 2:
        display_employee()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        update_employee()
    elif choice == 5:
        delete_employee()
    elif choice == 6:
        print("Thank you for using this program")
        break
    else:
        print("Enter a valid choice")






























