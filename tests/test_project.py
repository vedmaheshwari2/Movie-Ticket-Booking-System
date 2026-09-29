import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from movies import get_all_seats
from credits import CreditManager
from booking import BookingManager

def test_seat_generation():
    seats = get_all_seats()
    assert len(seats) == 50
    assert seats[0] == "A1"
    assert seats[-1] == "E10"

def test_credit_calculation(tmp_path, monkeypatch):
    manager = CreditManager()
    manager.credits = {}
    assert manager.add_credits("Test User", 4) == 60
    assert manager.get_balance("Test User") == 60

def test_bulk_discount():
    from movies import MOVIES
    manager = BookingManager()
    booking = manager.create_booking(
        "Test User", MOVIES[1], 5,
        ["A1", "A2", "A3", "A4", "A5"], 0, 75, 75
    )
    assert booking.bulk_discount == 187.5
    assert booking.final_amount == 1062.5
