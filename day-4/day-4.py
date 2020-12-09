'''
    PROCESS INPUTS
'''

# Open and parse input text
f = open("passports.txt", "r")
passports = [sorted(x.replace("\n", " ").split()) for x in list(f.read().split("\n\n"))]



'''
    PART 1: VALIDATE PASSPORTS

    Complexity: O(n^2)

    For this part, the algorithm only needs to count the number of fields and consider CID as optional.
'''
'''
valid_passports = 0

for passport in passports:
    # Cover the three possible cases of valid passports
    # 1. Has eight fields (automatically valid)
    # 2. Has seven fields, but doesn't have BYR (in which CID will be the first field)
    # 3. Has seven fields, but has BYR (in which CID will be the second field)
    if (len(passport) == 8) or ((len(passport) == 7) and ("cid" not in passport[0]) and ("cid" not in passport[1])):
        valid_passports += 1

print(valid_passports)
'''


'''
    PART 2: VALIDATE PASSPORTS

    Complexity: O(n^3)

    For this part, the algorithm not only needs to perform part 1, but must also validate the value at each field.
    The algorithm uses a set of predefined validators and calls them from a dictionary.
'''

def validate_byr (byr):
    try:
        return 1920 <= int(byr) <= 2002
    except ValueError:
        return False

def validate_ecl (ecl):
    return (ecl in "amb blu brn gry grn hzl oth")

def validate_eyr (eyr):
    try:
        return 2020 <= int(eyr) <= 2030
    except ValueError:
        return False

def validate_hcl (hcl):
    if (hcl[0] == "#") and (len(hcl) == 7):
        hcl = hcl[1:]

        # Adds up all the valid characters in the hair colour
        # If the total sum is 6, then all characters are valid
        return (sum([1 if ((48 <= ord(letter) <= 57) or (97 <= ord(letter) <= 102)) else 0 for letter in hcl]) == 6)

    return False

def validate_hgt (hgt):
    try:
        measurement_type = hgt[-2:]
        height = int(hgt[:-2])
    except ValueError:
        return False

    # Check valid range dependent on the measurement type
    return ((150 <= height <= 193) if measurement_type == "cm" else (59 <= height <= 76) if measurement_type == "in" else False)

def validate_iyr (iyr):
    try:
        return 2010 <= int(iyr) <= 2020
    except ValueError:
        return False

def validate_pid (pid):
    return (sum([1 if (48 <= ord(letter) <= 57) else 0 for letter in pid]) == 9)
    
# Dictionary of validation functions
validators = {
    "byr": validate_byr,
    "cid": lambda x: True,
    "ecl": validate_ecl,
    "eyr": validate_eyr,
    "hcl": validate_hcl,
    "hgt": validate_hgt,
    "iyr": validate_iyr,
    "pid": validate_pid
}

valid_passports = 0

for passport in passports:
    # Cover the three possible cases of valid passports
    # 1. Has eight fields (automatically valid)
    # 2. Has seven fields, but doesn't have BYR (in which CID will be the first field)
    # 3. Has seven fields, but has BYR (in which CID will be the second field)
    if (len(passport) == 8) or ((len(passport) == 7) and ("cid" not in passport[0]) and ("cid" not in passport[1])):
        valid_current = True
        
        # Check each field
        for field in passport:
            field_type, field_value = field.split(":")

            # If one of the fields is invalid, no need to check the rest
            # Break out and consider the current passport in question invalid
            if validators[field_type](field_value) is not True:
                valid_current = False
                break

        # If it passed all the validity checks, count
        if valid_current:
            valid_passports += 1

print(valid_passports)