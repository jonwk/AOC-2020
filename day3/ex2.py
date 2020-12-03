f = open('input.txt', 'r')
data = [line.strip() for line in f.readlines()]


def traverse(right, down):
    x = 0
    total = 0
    for i in range(len(data)):
        if i % down != 0:
            continue
        if data[i][x] == '#':
            total = total + 1
        x = (x + right) % len(data[0])
    return total   

print("Right 1, down 1 =",traverse(1,1))
print("Right 3, down 1 =",traverse(3,1))
print("Right 5, down 1 =",traverse(5,1))
print("Right 7, down 1 =",traverse(7,1))
print("Right 1, down 2 =",traverse(1,2))
print("Product of everything =",(traverse(1,1)*traverse(3,1)*traverse(5,1)*traverse(7,1)*traverse(1,2)))
