# Movie Ticket Booking System

## Overview
A Python-based console movie ticket booking system that manages movie selection, ticket quantities, free-ticket offers, seat selection, Friday/bulk discounts, persistent movie credits, and booking records.

## Problem
Manual movie booking can cause calculation errors, duplicate seat selection, and poor tracking of customer rewards. This project provides a structured digital workflow for booking tickets and managing credits.

## Features
- Customer identification and returning-customer credits
- Movie selection with ticket prices
- Paid and free ticket calculation
- Seat selection with duplicate/invalid-seat validation
- Persistent seat occupancy using JSON booking storage
- 10% Friday discount
- 15% bulk discount for more than 4 paid tickets
- 15 movie credits per paid ticket
- 90 credits can be exchanged for one free ticket
- Booking ID and booking receipt
- Input validation and error handling
- Modular Python architecture
- Basic automated tests

## Technologies
- Python 3
- JSON
- Object-oriented programming
- Dataclasses
- File handling
- Exception handling
- Pytest-compatible tests

## Project Structure
```text
Movie_Ticket_Booking_Project/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── storage.py
│   ├── validation.py
│   ├── movies.py
│   ├── credits.py
│   └── booking.py
├── tests/
│   ├── __init__.py
│   └── test_project.py
├── data/
│   ├── movie_credits.json
│   └── bookings.json
├── docs/
├── requirements.txt
├── README.md
└── statement.md
```

## How to Run
1. Install Python 3.10 or newer.
2. Open a terminal in the project folder.
3. Run:
   `python src/main.py`
4. Enter the customer name, select a movie, enter ticket quantity, and choose seats.

## Testing
If pytest is installed:
`pytest`

The tests cover seat generation, movie-credit calculation, and bulk-discount calculation.

## GitHub
Create a repository, add all project files, and use meaningful commits such as:
- Initial project structure
- Added booking and seat management
- Added credit system
- Added validation and tests
- Added documentation and diagrams
