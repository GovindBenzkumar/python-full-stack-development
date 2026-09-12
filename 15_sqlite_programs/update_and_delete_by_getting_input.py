import sqlite3

con = sqlite3.connect('sampledb')

#con.execute("create table student2(roll int, name text, age int)")
#con.execute("insert into student2 values (101,'Amal',23),(102,'Ebin',24)")
#n= input("Enter new Name:")
#a= int(input("Enter new Age:"))
r= int(input("Enter the existing Roll no:"))
#con.execute("update student2 set name=? ,age=? where roll=?",(n,a,r))

con.execute("delete from student2 where roll=?",(r,))
con.commit()

d= con.execute('select * from student2')
for roll,name,age in d:
    print("Roll:",roll)
    print("Name:",name)
    print("Age:",age)
    print("-----------")