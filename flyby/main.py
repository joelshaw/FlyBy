from .location import get_location
from .flights import get_flights_overhead
from .formatter import format_flight


def main():
    lat, lon = get_location()
    flights = get_flights_overhead(lat, lon)

    if not flights:
        print("There are no flights currently overhead.")
    for flight in flights:
        print(format_flight(flight))
