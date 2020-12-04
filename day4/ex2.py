import re
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
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def eval_byr(year):
    return (len(year)==4) and (int(year) in range(1920,2003))
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def eval_iyr(year):
    return (len(year)==4) and (int(year) in range(2010,2021))
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def eval_eyr(year):
    return (len(year)==4) and (int(year) in range(2020,2031))
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
def eval_hgt(hgt):
    return (hgt.endswith('cm') and int(hgt[:-2]) in range(150,194)) or (hgt.endswith('in') and int(hgt[:-2]) in range(59,77))
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def eval_hcl(hcl):
    return re.match(r'^#[0-9a-f]{6}$', hcl)
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def eval_ecl(ecl):
    return ecl in ('amb','blu','brn','gry','grn','hzl','oth')
# pid (Passport ID) - a nine-digit number, including leading zeroes.
def eval_pid(pid):
    return len(pid) == 9 and re.match(r'^[0-9]{9}$', pid)
# cid (Country ID) - ignored, missing or not.
def eval_passport(line):
    return eval_byr(line['byr']) and eval_iyr(line['iyr']) and eval_eyr(line['eyr']) and eval_hgt(line['hgt']) and eval_hcl(line['hcl']) and eval_ecl(line['ecl']) and eval_pid(line['pid'])

f = open('input.txt', 'r')
data = [line.strip() for line in f.readlines()]

batch_file = parse(data)

valid_passsports = 0

for line in batch_file:
    if(all(valid_fields in line for valid_fields in ('byr', 'iyr','eyr', 'hgt','hcl', 'ecl','pid'))):
        if(eval_passport(line)):
            valid_passsports+=1
            print("------Valid-Passport------")
            print(line)

print("Total Valid Passports =", valid_passsports)
