from string import ascii_lowercase as letters

f = open('input.txt', 'r')
data = f.read()

# def split_data(data):
#     yield from data.split("\n\n")

# def split_group(group):
#     return group.splitlines()

# # split_data(data) # Test
def same_answers(data):
    return sum(all([letter in person for person in data.splitlines()]) for letter in letters)

def sum_of_new_customs(data):
    return sum(same_answers(group) for group in data)

print("Total sum of customs in the new order is",sum_of_new_customs(data.split("\n\n")))