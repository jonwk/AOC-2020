# Using readlines() 
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
input_Arr = []
# Strips the newline character 
for line in Lines: 
    input_Arr.append(int(line.strip()))

for element1 in input_Arr:
    for element2 in input_Arr:
        for element3 in input_Arr:
            if(element1+element2+element3==2020):
                print("element1 - ",element1," element2 - ",element2," element3 - ",element3, "Product of 3 elements = ",element1*element2*element3)
