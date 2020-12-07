from string import ascii_lowercase as letters

f = open('input.txt', 'r')
data = f.read()

def split_data(data):
    yield from data.split("\n\n")

# split_data(data) # Test

def sum_of_customs(data):
    return sum(letter in group for letter in letters for group in split_data(data))

print("Total sum of customs",sum_of_customs(data))
