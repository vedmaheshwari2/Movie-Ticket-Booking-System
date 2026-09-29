from models import Movie

MOVIES = {
    1: Movie(1, "Avengers: Endgame", 250),
    2: Movie(2, "Interstellar", 300),
    3: Movie(3, "Inception", 280),
    4: Movie(4, "Spider-Man: No Way Home", 220)
}

def display_movies():
    print("\nAvailable Movies")
    print("-" * 55)
    for number, movie in MOVIES.items():
        print(f"{number}. {movie.name} - Rs.{movie.price:.2f}")

def get_all_seats():
    return [f"{row}{number}" for row in "ABCDE" for number in range(1, 11)]
