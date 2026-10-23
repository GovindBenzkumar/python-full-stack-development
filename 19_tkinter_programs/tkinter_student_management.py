from tkinter import *
import sqlite3
con = sqlite3.connect('sample.db')
con.execute("create table if not exists student1 (name text,age int,rollno int)")


sample=Tk()
sample.geometry("300x300")
n1=Label(sample,text="Name")
n1.place(x=20,y=30)
n=Entry(sample)
n.place(x=80,y=30)
a1=Label(sample,text="Age")
a1.place(x=20,y=50)
a=Entry(sample)
a.place(x=80,y=50)
r1=Label(sample,text="Roll No")
r1.place(x=20,y=70)
r=Entry(sample)
r.place(x=80,y=70)
s1=Label(sample,text="Search")
s1.place(x=80,y=200)
s=Entry(sample)
s.place(x=130,y=200)

def add():
    x=n.get()
    y=int(a.get())
    z=int(r.get())
    con.execute("insert into student1 values (?,?,?)",(x,y,z))
    con.commit()

btn=Button(sample,text="add",command=add)
btn.place(x=20,y=100)
def display():
    d=con.execute("select * from student1")
    for x in d:
        label = Label(sample, text=f"Name :{x[0]}")
        label.pack()
        label = Label(sample, text=f"Age :{x[1]}")
        label.pack()
        label = Label(sample, text=f"Roll no :{x[2]}")
        label.pack()

btn=Button(sample,text="display",command=display)
btn.place(x=80,y=100)
def search():
    t=int(s.get())
    d=con.execute("select * from student1 where rollno=?",(t,))
    for x in d:
        label = Label(sample, text=f"Name :{x[0]}")
        label.pack()
        label = Label(sample, text=f"Age :{x[1]}")
        label.pack()
        label = Label(sample, text=f"Roll no :{x[2]}")
        label.pack()
btn=Button(sample,text="search",command=search)
btn.place(x=150,y=230)

sample.mainloop()