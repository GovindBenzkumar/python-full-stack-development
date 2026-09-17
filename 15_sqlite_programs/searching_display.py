import sqlite3

con = sqlite3.connect('sampledb2')

r= int(input("Enter an existing Roll Number:"))
#con.execute("create table student1(roll int, name text, age int)")
#con.execute("insert into student1 values (101,'Amal',23),(102,'Ebin',24)")
con.commit()

d= con.execute("select * from student where roll=?",(r,))
for roll,name,age in d:
    print("Roll:",roll)
    print("Name:",name)
    print("Age:",age)
    print("------------")