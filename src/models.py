from dataclasses import dataclass, field
from typing import List

@dataclass
class Movie:
    movie_id: int
    name: str
    price: float

@dataclass
class Booking:
    booking_id: str
    customer_name: str
    movie_name: str
    ticket_price: float
    paid_tickets: int
    paid_seats: List[str]
    free_seats: List[str]
    subtotal: float
    friday_discount: float
    bulk_discount: float
    final_amount: float
    credits_earned: int
    total_credits: int
