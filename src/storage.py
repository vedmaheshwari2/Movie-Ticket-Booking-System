import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CREDIT_FILE = DATA_DIR / "movie_credits.json"
BOOKING_FILE = DATA_DIR / "bookings.json"

def _load(path, default):
    DATA_DIR.mkdir(exist_ok=True)
    if not path.exists():
        return default
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return default

def _save(path, data):
    DATA_DIR.mkdir(exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_credits():
    return _load(CREDIT_FILE, {})

def save_credits(credits):
    _save(CREDIT_FILE, credits)

def load_bookings():
    return _load(BOOKING_FILE, [])

def save_booking(booking):
    bookings = load_bookings()
    bookings.append(booking)
    _save(BOOKING_FILE, bookings)
