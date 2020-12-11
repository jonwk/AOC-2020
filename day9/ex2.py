with open("input.txt") as file:
    data = [int(line) for line in file]


def check(n):
    for j in preamble25:
        if n-j in preamble25 and n-j != j:
            return False
    return True

numbers = data[25:]
firstInvalidNumber = None
for i in range(len(numbers)):

    preamble25 = data[i:i+25]

    if check(numbers[i]):
        firstInvalidNumber = numbers[i]
        break

encryptionWeakness, line = None, None
for i in range(len(data)):

    line_sum = 0
    length = 2

    while line_sum < firstInvalidNumber:

        line = data[i:i + length]
        line_sum = sum(line)
        length += 1

    if line_sum == firstInvalidNumber:
        encryptionWeakness = min(line) + max(line)
        break

print("encryption weakness in this XMAS-encrypted list of numbers -", encryptionWeakness)