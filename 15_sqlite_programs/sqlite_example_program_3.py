import sqlite3

con = sqlite3.connect('sampledb3')


#con.execute("create table student(roll int, name text, age int)")
#con.execute("insert into student values (101,'Amal',23),(102,'Ebin',24)")
l= int(input("Enter the limit of entries you want to enter:"))
for i in range(l):
    r= int(input("Enter roll number: "))
    n= input("Enter name: ")
    a= int(input("Enter age: "))
    con.execute("insert into student values(?,?,?)",(r,n,a))
    con.commit()

    d= con.execute('select * from student')
    for roll, name, age in d:
        print("Roll:", roll)
        print("Name:", name)
        print("Age:", age)
        print("-----------")