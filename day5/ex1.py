f = open('input.txt', 'r')
data = [line.strip() for line in f.readlines()]

def split_line(line: str):
    row_b, col_b = line[:-3], line[-3:]
    return row_b, col_b

# for line in data:
#     print(split_line(line))    

def map_to_bin(s, map_0="L", map_1="R"):
    remapped = s.replace(map_0, "0").replace(map_1, "1")
    return int(remapped, 2)

def seat_num(line):
    row_b, col_b = split_line(line)
    row, col = map_to_bin(row_b, "F", "B"), map_to_bin(col_b)
    return row * 8 + col

def max_seat_id(data):
    return max(seat_num(line) for line in data)

print("The highest seat ID is",max_seat_id(data))