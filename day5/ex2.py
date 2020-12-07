f = open('input.txt', 'r')
data = [line.strip() for line in f.readlines()]

def split_line(line: str):
    row_b, col_b = line[:-3], line[-3:]
    return row_b, col_b

def map_to_bin(s, map_0="L", map_1="R"):
    remapped = s.replace(map_0, "0").replace(map_1, "1")
    return int(remapped, 2)

def seat_num(line):
    row_b, col_b = split_line(line)
    row, col = map_to_bin(row_b, "F", "B"), map_to_bin(col_b)
    return row * 8 + col

def get_seats_from_data(data):
    return (seat_num(line) for line in data)

def get_my_seat(min_seat, max_seat, seats):
    return [seat for seat in range(min_seat, max_seat+1) if seat not in seats][0]


seats = list(get_seats_from_data(data))

min_seat,max_seat = min(seats), max(seats)

print("My seat ID is",get_my_seat(min_seat, max_seat, seats))