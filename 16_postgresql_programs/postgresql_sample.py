import psycopg2

con = psycopg2.connect(user='postgres',password='134340',host='localhost',port='5432',database='sample')
con.autocommit = True
cur = con.cursor()
#cur.execute("create database sample")
#cur.execute("create table student(roll int,name text,age int)")
#cur.execute("insert into student values(1,'anal',23)")
cur.execute("select * from student")
d = cur.fetchall()
for i in d:
    print(i)
print("database created")