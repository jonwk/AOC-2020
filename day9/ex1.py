with open("input.txt") as file:
    data = [int(line) for line in file]


def check(n):
    for j in preamble25:
        if n-j in preamble25 and n-j != j:
            return False
    return True

numbers = data[25:]
firstInvaidNumber = None
for i in range(len(numbers)):

    preamble25 = data[i:i+25]

    if check(numbers[i]):
        firstInvaidNumber = numbers[i]
        break


print("first number which is not the sum of two of the 25 numbers before it -", firstInvaidNumber)
