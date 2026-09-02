t_id= 1
class BusReservation:
    def add_bus(self):
        self.bus_name= input("Enter the bus name")
        self.bus_number= input("Enter the bus registration number")
        self.price= int(input("Enter the ticket price of the bus seat"))
        self.seat= int(input("Enter the total number of seats available"))

    def display_buses(self):
        print("Name of bus=",self.bus_name)
        print("Registration number of bus=",self.bus_number)
        print("Ticket price per seat=",self.price)
        print("Total number of seats available=",self.seat)

    def book_seat(self):
        self.name= input("Enter your name:")
        self.age= input("Enter your age:")
        self.bus_name= input("Select your bus:")

    def display_tickets(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Bus chosen=",self.bus)

    def cancel_seat(self):
        self.t_id= input("Enter your ticket ID:")

bus=[]
tickets=[]
while True:

    print("Bus reservation system for route from Ekm to Tvm")
    print(" 1.Add buses( For admin use only!)\n2.View Buses\n3.Book Seat\n4.Display bookings\n4.Cancel Seat\n5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        obj = BusReservation()
        obj.add_bus()
        bus.append(obj)
    if choice==2:
        for i in bus:
            i.display_buses()
    if choice==3:
        global t_id
        name= input("Enter your name:")
        age= input("Enter your age:")
        bus_name= input("Select your bus:")
        for i in bus:
            if i.seat>0:


b