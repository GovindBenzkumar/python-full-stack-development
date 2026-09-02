#single inheritance

'''''class Person:
    def display(self):
        print("hai")
class Student(Person):
    def show(self):
        print("hello")

obj = Student()
obj.display()'''

#multiple inheritance

'''class A:
    def display(self):
        print("hello")
class B:
    def show(self):
        print("hai")
class C(A,B):
    def move(self):
        print("wings")

obj = C()
obj.display()
obj.show()
obj.move()'''

#Multilevel Inheritance

'''class A:
    def display(self):
        print("hai")
class B(A):
    def display1(self):
        print("hello")
class C(B):
    def display2(self):
        print("dynamite")
class D(C):
    def display3(self):
        print("mic drop")

obj= D()
obj.display()
obj.display1()
obj.display2()
obj.display3()'''

#Hierarchical Inheritance

class A:
    def display(self):
        print("hai")
class B(A):
    def display1(self):
        print("hello")
class C(A):
    def display2(self):
        print("dynamite")
class D(A):
    def display3(self):
        print("Aliens")
obj= D()
obj.display()
obj1= C()
obj1.display()
obj2=B()
obj2.display()







