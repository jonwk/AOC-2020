file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
input_Arr = []

# # Strips the newline character 
for line in Lines: 
    input_Arr.append(line.replace("\n", ""))


y = 0
X = 0
for inp in input_Arr:
    print(inp)
    if y > 30:
        y = y - 31
    if inp[y] == '#':
        X = X + 1
    y = y + 3

print("Total Trees in the way X =",X)
