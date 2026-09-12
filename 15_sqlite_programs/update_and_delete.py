import sqlite3

con = sqlite3.connect('sampledb')

#con.execute("create table student1(roll int, name text, age int)")
#con.execute("insert into student1 values (101,'Amal',23),(102,'Ebin',24)")
#con.execute("update student1 set name='Abhi',age=23 where roll=101")
con.execute("delete from student1 where roll=101")
con.commit()

d= con.execute('select * from student1')
for roll,name,age in d:
    print("Roll:",roll)
    print("Name:",name)
    print("Age:",age)
    print("-----------")