import sqlite3
con= sqlite3.connect("sampledb6")
'''con.execute("create table fruits(id int,name text)")
con.execute("insert into fruits values (1,'apple'),(2,'orange'),(3,'banana'),(4,'papaya'),(5,'cherry')")
con.execute("create table booking(id int,price int)")
con.execute("insert into booking values (2,200),(8,100),(4,110),(6,120),(5,130),(10,140)")'''
con.commit()
'''d=con.execute("select * from fruits")
for i in d:
    print(i)
e=con.execute("select * from booking")
for i in e:
    print(i)'''

'''d=con.execute("select fruits.name,booking.price from fruits inner join booking on fruits.id= booking.id")
for i in d:
    print(i)'''

'''d=con.execute("select fruits.name,booking.price from fruits left outer join booking on fruits.id= booking.id")
for i in d:
    print(i)'''

'''d=con.execute("select fruits.name,booking.price from fruits right outer join booking on fruits.id= booking.id")
for i in d:
    print(i)'''

d=con.execute("select fruits.name,booking.price from fruits full outer join booking on fruits.id= booking.id")
for i in d:
    print(i)


