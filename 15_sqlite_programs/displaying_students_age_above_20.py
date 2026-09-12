import sqlite3

con = sqlite3.connect('sampledb2')

#con.execute("create table student2(roll int, name text, age int)")
#con.execute("insert into student2 values (101,'Amal',23),(102,'Ebin',24),(103,'Abhay',20),(104,'Gokul',19),(105,'Achyut',16),(106,'Jungkook',10)")
#con.commit()

d= con.execute("select * from student2 where age>20")
for roll,name,age in d:
    print("Roll:",roll)
    print("Name:",name)
    print("Age:",age)
    print("-----------")