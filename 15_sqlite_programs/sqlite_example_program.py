import sqlite3

con = sqlite3.connect('sampledb')#connection object


#con.execute("create table student(roll int, name text, age int)")#table creation
#con.execute("insert into student values (101,'Amal',23),(102,'Ebin',24)")#table insertion
#con.commit()#save

d= con.execute('select * from student')#displaying table
for i in d:
    print(i)
print("created")