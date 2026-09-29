from movies import MOVIES, display_movies, get_all_seats
from validation import get_positive_integer, get_movie_choice, get_seat_selection
from credits import CreditManager
from booking import BookingManager

def main():
    print("=" * 55)
    print("MOVIE TICKET BOOKING SYSTEM")
    print("=" * 55)

    name = input("\nEnter your name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    credit_manager = CreditManager()
    booking_manager = BookingManager()

    current_credits = credit_manager.get_balance(name)

    if name in credit_manager.credits:
        print(f"\nWelcome back, {name}!")
        print(f"You have {current_credits} movie credits.")
    else:
        print(f"\nWelcome, {name}!")

    credit_free_ticket = False
    if current_credits >= 90:
        use_credit = input(
            "\nYou have enough credits for a free ticket. Use 90 credits? (yes/no): "
        ).strip().lower()
        if use_credit == "yes":
            credit_free_ticket = credit_manager.use_free_ticket(name)
            if credit_free_ticket:
                print("Free ticket added!")

    display_movies()
    choice = get_movie_choice(MOVIES)
    movie = MOVIES[choice]
    tickets = get_positive_integer("\nEnter number of tickets: ")

    free_tickets = 1 if tickets > 2 else 0
    if tickets > 4:
        free_tickets = 1
    if credit_free_ticket:
        free_tickets += 1

    total_seats = tickets + free_tickets
    all_seats = get_all_seats()
    occupied = booking_manager.occupied_seats()
    available = [seat for seat in all_seats if seat not in occupied]

    print(f"\nYou need to select {total_seats} seats.")
    print("Available Seats:")
    print(", ".join(available))

    if len(available) < total_seats:
        print("Not enough seats are available.")
        return

    selected = get_seat_selection(available, total_seats)
    earned = credit_manager.add_credits(name, tickets)
    total_credits = credit_manager.get_balance(name)

    booking = booking_manager.create_booking(
        name, movie, tickets, selected, free_tickets, earned, total_credits
    )
    booking_manager.print_receipt(booking)
    print(credit_manager.balance_message(name))

if __name__ == "__main__":
    main()
