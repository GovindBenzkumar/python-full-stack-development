buses = [
    ["Kochi-Trivandrum", 40]
]

bookings = []


class Bus:

    def add_bus(self):
        route = input("Enter route: ")
        seats = int(input("Enter number of seats: "))

        buses.append([route, seats])

        print("Bus added successfully!")

    def view_buses(self):
        print("\n--- BUS DETAILS ---")

        for i in range(len(buses)):
            print("Bus ID:", i + 1)
            print("Route:", buses[i][0])
            print("Available Seats:", buses[i][1])
            print("------------------")

    def book_seat(self):
        bus_id = int(input("Enter Bus ID: "))

        if bus_id <= 0 or bus_id > len(buses):
            print("Invalid Bus ID")
            return

        # Seat availability
        if buses[bus_id - 1][1] > 0:
            name = input("Enter passenger name: ")

            buses[bus_id - 1][1] -= 1

            bookings.append([name, bus_id])

            print("Seat booked successfully!")
            print("Available seats:", buses[bus_id - 1][1])

        else:
            print("No seats available!")


bus = Bus()

while True:

    print("\n===== BUS RESERVATION SYSTEM =====")
    print("1. Add Buses")
    print("2. View Buses")
    print("3. Book Seat")
    print("4. Cancel Booking")
    print("5. Display Bookings")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bus.add_bus()

    elif choice == 2:
        bus.view_buses()

    elif choice == 3:
        bus.book_seat()

    elif choice == 4:
        print("Cancel Booking")

    elif choice == 5:
        print("Display Bookings")

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice")














