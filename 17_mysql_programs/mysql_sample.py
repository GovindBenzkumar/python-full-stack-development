import mysql.connector
con = mysql.connector.connect(user='root', password='134340',database='sample_db')
cur = con.cursor()
#cur.execute("create table student(roll int, name text)")
#cur.execute("insert into student values(102,'Ebin'),(103,'Achu')")
#cur.execute("update student set name='Joel' where roll=102")
#cur.execute("delete from student where roll=102")
#cur.execute("create table teacher(name text, subject text)")
#cur.execute("insert into teacher values('Amrita','Math'),('Govind','English')")
#cur.execute("alter table student add column subject text")
#cur.execute("update student set subject='Math' where roll=101")
cur.execute("update student set subject='English' where roll=103")
#inner join
cur.execute("select student.name,teacher.name from student inner join teacher on student.subject=teacher.subject")
d=cur.fetchall()
for i in d:
    print(i)
