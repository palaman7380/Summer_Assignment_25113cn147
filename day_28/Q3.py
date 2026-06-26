class TicketBooking:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.bookings = []

    def book_ticket(self, name, seats):
        if seats > self.available_seats:
            print("Not enough seats available!")
        else:
            self.bookings.append({"name": name, "seats": seats})
            self.available_seats -= seats
            print(f"Ticket booked for {name} - {seats} seat(s).")

    def cancel_ticket(self, name):
        for booking in self.bookings:
            if booking["name"] == name:
                self.available_seats += booking["seats"]
                self.bookings.remove(booking)
                print(f"Booking cancelled for {name}.")
                return
        print("Booking not found!")

    def display(self):
        print(f"Available Seats: {self.available_seats}/{self.total_seats}")
        print("Current Bookings:")
        for b in self.bookings:
            print(f"  {b['name']} - {b['seats']} seat(s)")



show = TicketBooking(10)
show.book_ticket("Amit", 3)
show.book_ticket("Priya", 5)
show.display()
show.cancel_ticket("Amit")
show.display()