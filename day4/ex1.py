f = open('input.txt', 'r')
data = [line.strip() for line in f.readlines()]

i=1
batch_file = data.split("\n")

for line in batch_file:
    print(line)
