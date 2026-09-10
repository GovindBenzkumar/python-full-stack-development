import sqlite3

con = sqlite3.connect('sampledb2')


con.execute("create table student(roll int, name text, age int)")
con.execute("insert into student values (101,'Amal',23),(102,'Ebin',24)")
con.commit()

d= con.execute('select * from student')
for roll,name,age in d:
    print("Roll:",roll)
    print("Name:",name)
    print("Age:",age)
    print("-----------")