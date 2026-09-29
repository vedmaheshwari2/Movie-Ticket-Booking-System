from datetime import datetime
import random
from models import Booking
from storage import load_bookings, save_booking

class BookingManager:
    def __init__(self):
        self.bookings = load_bookings()

    def occupied_seats(self):
        occupied = set()
        for booking in self.bookings:
            occupied.update(booking.get("paid_seats", []))
            occupied.update(booking.get("free_seats", []))
        return occupied

    def create_booking(self, name, movie, paid_tickets, selected_seats,
                       free_tickets, credits_earned, total_credits):
        paid_seats = selected_seats[:paid_tickets]
        free_seats = selected_seats[paid_tickets:]
        subtotal = paid_tickets * movie.price
        friday_discount = subtotal * 0.10 if datetime.now().strftime("%A") == "Friday" else 0
        bulk_discount = subtotal * 0.15 if paid_tickets > 4 else 0
        total_discount = friday_discount + bulk_discount
        final_amount = subtotal - total_discount
        booking_id = "MOV" + str(random.randint(10000, 99999))

        booking = Booking(
            booking_id, name, movie.name, movie.price, paid_tickets,
            paid_seats, free_seats, subtotal, friday_discount,
            bulk_discount, final_amount, credits_earned, total_credits
        )
        data = booking.__dict__
        save_booking(data)
        return booking

    def print_receipt(self, booking):
        print("\n" + "=" * 55)
        print("BOOKING CONFIRMED")
        print("=" * 55)
        print(f"Booking ID    : {booking.booking_id}")
        print(f"Name          : {booking.customer_name}")
        print(f"Movie         : {booking.movie_name}")
        print(f"Ticket Price  : Rs.{booking.ticket_price:.2f}")
        print("\nPaid Tickets")
        print(f"Number        : {booking.paid_tickets}")
        print(f"Seats         : {', '.join(booking.paid_seats)}")
        if booking.free_seats:
            print("\nFree Tickets")
            print(f"Seats         : {', '.join(booking.free_seats)}")
        print("\n" + "-" * 55)
        print(f"Subtotal       : Rs.{booking.subtotal:.2f}")
        if booking.friday_discount:
            print(f"Friday Discount: -Rs.{booking.friday_discount:.2f}")
        if booking.bulk_discount:
            print(f"Bulk Discount  : -Rs.{booking.bulk_discount:.2f}")
        print(f"Total Discount : Rs.{booking.friday_discount + booking.bulk_discount:.2f}")
        print(f"Final Amount   : Rs.{booking.final_amount:.2f}")
        print("\n" + "=" * 55)
        print("MOVIE CREDIT SYSTEM")
        print("=" * 55)
        print(f"Credits Earned : +{booking.credits_earned}")
        print(f"Total Credits  : {booking.total_credits}")
        print("=" * 55)
        print("Thank you for booking with us!")
        print("=" * 55)
