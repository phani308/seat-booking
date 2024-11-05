import sys
from seat_helpers import init_seats, track_seats, seat_id, reserve, cancel

def main():
    try:
        seats = init_seats()  # Load seats into memory

        # CLI args validation
        if len(sys.argv) != 4:
            raise ValueError("Invalid number of arguments")

        action = sys.argv[1].upper()
        starting_seat = sys.argv[2]
        num_seats = int(sys.argv[3])

        # Parse the row and seat index
        row, start_seat = seat_id(starting_seat)

        # Based on the action, reserve or cancel seats
        if action == "BOOK":
            result = reserve(seats, row, start_seat, num_seats)
        elif action == "CANCEL":
            result = cancel(seats, row, start_seat, num_seats)
        else:
            raise ValueError("Invalid action")

        # Save the seat state to tracking file
        track_seats(seats)
        print(result)
    except Exception:
        print("FAIL")

if __name__ == "__main__":
    main()
