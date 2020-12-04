def parse(lines):
    parsed_data = {}
    for line in lines:
        if line.strip():
            for word in line.split():
                if ':' in word:
                    key, value = word.split(':', 1)
                    parsed_data[key] = value
        else:
            yield parsed_data
            parsed_data = {}
    yield parsed_data

f = open('input.txt', 'r')
data = [line.strip() for line in f.readlines()]

batch_file = parse(data)

valid_passsports = 0

for line in batch_file:
    if(all(valid_fields in line for valid_fields in ('eyr', 'hgt', 'byr', 'iyr', 'pid','hcl', 'ecl',))):
        valid_passsports+=1
        # print("------Valid-Passport------")
        # print(line)
    # else:
    #     print("------Invalid-Passport------")
    #     print(line)

print("Total Valid Passports =", valid_passsports)
