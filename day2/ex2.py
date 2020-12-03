
def evaluate_password(min, max, letter, password):
    count = 0
    if password[min-1] == letter :
        count = count + 1
    if password[max-1] == letter :
        count = count + 1
    return count == 1 

file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
input_Arr = []

# Strips the newline character 
for line in Lines: 
    input_Arr.append(line.strip())

valid_password_count = 0

for inp in input_Arr:
    condition, password = inp.split(': ')
    atleast, rest = condition.split('-') 
    atmost, letter = rest.split(' ')
    if (evaluate_password(int(atleast),int(atmost),letter, password)):
        print("Valid Password condition",condition,"password", password)
        valid_password_count = valid_password_count + 1

print("Total Passwords: ", len(input_Arr)," Valid Passwords: ",valid_password_count)
