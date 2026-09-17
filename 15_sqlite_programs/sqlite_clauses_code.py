import sqlite3
con= sqlite3.connect("sampledb5")
#con.execute("create table student(roll int, name text, age int)")
#con.execute("insert into student values (101,'Amal',23),(102,'Ebin',24),(103,'Gokul',19),(104,'Amrita',21),(105,'Prasanti',22)")
con.commit()
#d= con.execute("select * from student where roll%2==0 and age>20")
#d= con.execute("select * from student where age>20 and age<30 order by roll desc ")
d= con.execute("select * from student where name like 'a%' order by age desc")

for i in d:
    print(i)

