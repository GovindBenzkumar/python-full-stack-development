from tkinter import *


sample = Tk()
sample.geometry("400x500")
sample.title("welcome")
sample.resizable(True,False)
sample.configure(bg="pink")

#widgets

l1 = Label(sample,text="Name",font=("Times New Roman",10),bg="white")
# l1.pack(side=LEFT)
l1.place(x=30,y=50)

e1 = Entry(sample,font=("Times New Roman",10),bg="white")
e1.place(x=110,y=50)

def display():
    new = Toplevel(sample)


    new.geometry("400x500")
    new.title("welcome")

    new.mainloop()


    # x  = e1.get()
    #
    # l2 = Label(sample,text=x,bg="green")
    # l2.pack()

b = Button(sample,text="click",font=("Times New Roman",10),bg="white",activebackground="red",command=display)
b.place(x=110,y=90)
sample.mainloop()


#tkinter javatpoint