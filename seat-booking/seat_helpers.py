import os
import json

rows = 20
## This represent the seat layout for each row
seat_layout = [2, 4, 2] 
seat_file = "seat_reservations.json"

def init_seats():
    ## Init and Load the seat reservation from a json file ##
    if os.path.exists(seat_file):
        with open(seat_file, 'r') as f:
            return json.load(f)
    else:
        seats = {chr(ord('A') + row): [0] * sum(seat_layout) for row in range(rows)}
        track_seats(seats)
        return seats

def track_seats(seats):
   ## tracks the seat reservation using a json file ##
    with open(seat_file, 'w') as f:
        json.dump(seats, f)

def seat_id(seat):
    ## Seat ID is a combination of row and seat number ##
    row = seat[0]
    seat_number = int(seat[1:])
    return row, seat_number

def reserve(seats, row, start_seat, num_seats):
   ## Book the seats when requested ##
    if row not in seats or start_seat + num_seats > len(seats[row]):
        return "FAIL"

    ## check seat availability ##
    if all(seat == 0 for seat in seats[row][start_seat:start_seat + num_seats]):
        for i in range(num_seats):
            seats[row][start_seat + i] = 1
        return "SUCCESS"
    else:
        return "FAIL"

def cancel(seats, row, start_seat, num_seats):
    ## Cancel the seats when requested ##
    if row in seats and all(seat == 1 for seat in seats[row][start_seat:start_seat + num_seats]):
        for i in range(num_seats):
            seats[row][start_seat + i] = 0
        return "SUCCESS"
    else:
        return "FAIL"