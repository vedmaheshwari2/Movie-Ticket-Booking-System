def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def get_movie_choice(movies):
    while True:
        try:
            choice = int(input("\nEnter movie number: "))
            if choice in movies:
                return choice
            print("Please select a valid movie.")
        except ValueError:
            print("Please enter a number.")

def get_seat_selection(available_seats, count):
    while True:
        selected = input(
            f"\nEnter {count} seat numbers separated by spaces: "
        ).upper().split()

        if len(selected) != count:
            print(f"Please enter exactly {count} seats.")
            continue

        if len(set(selected)) != count:
            print("You cannot select the same seat twice.")
            continue

        invalid = [seat for seat in selected if seat not in available_seats]
        if invalid:
            print("Invalid seat:", ", ".join(invalid))
            continue

        return selected
