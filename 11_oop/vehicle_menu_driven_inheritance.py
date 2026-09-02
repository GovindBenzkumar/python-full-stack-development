l = []

class vehicle:
    def data(self):
        self.number=int(input("enter your number:"))
        self.name=input("enter your vehicle name:")
        self.price=int(input("enter your price:"))
        self.wheels=int(input("enter your wheels:"))
class wheels (vehicle):
    def display(self):
        print("Vehicle number ",self.number)
        print("Vehicle Name ",self.name)


while True:
    print('''
    1.add vehicle
    2.display vehicle
    3.Exit
    ''')
    ch = int(input("Enter choice "))
    if ch==1:
        v1 = wheels()
        v1.data()
        l.append(v1)
    elif ch==2:
        while True:
            print('''
            1.2 wheels
            2.3 wheels
            3.4.wheels
            4.Exit
            ''')
            ch = int(input("Enter choice "))
            if ch == 1:
                c = 0
                for i in l:
                    if i.wheels == 2:
                        i.display()
                        c = 1
                if c==0:
                    print("Does not exists")
            elif ch == 2:
                c = 0
                for i in l:
                    if i.wheels == 3:
                        i.display()
                        c = 1
                if c==0:
                    print("Does not exists")
            elif ch == 3:
                c = 0
                for i in l:
                    if i.wheels == 4:
                        i.display()
                        c = 1
                if c==0:
                    print("Does not exists")
            elif ch==4:
                break
            else:
                print("Invalid choice")
    elif ch == 3:
        break
    else:
        print("Invalid choice")