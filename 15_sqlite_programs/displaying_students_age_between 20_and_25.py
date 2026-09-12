import sqlite3

con = sqlite3.connect('sampledb2')

#con.execute("create table student3(roll int, name text, age int)")
#con.execute("insert into student3 values (101,'Amal',23),(102,'Ebin',25),(103,'Abhay',20),(104,'Gokul',19),(105,'Achyut',16),(106,'Jungkook',29)")
#con.commit()

d= con.execute("select * from student3 where age>20 and age<25 ")
for roll,name,age in d:
    print("Roll:",roll)
    print("Name:",name)
    print("Age:",age)
    print("-----------")