import binascii

def read_passport_data():
    with open('four.input', 'r') as f:
        data = f.read()
    passport_list = data.split('\n\n')
    passport_list = [' '.join(tmp.split('\n')) for tmp in passport_list]
    return passport_list

def clear_passport_data(passport):
    for key, _ in passport.items():
        passport[key] = None
    return passport

def process_passports():
    passport_list = read_passport_data()
    passport_dict_list = []
    tmp_passport = {}
    for passport in passport_list:
        tmp_passport = {}
        for attr in passport.split(' '):
            tmp = attr.split(':')
            tmp_passport[tmp[0]] = tmp[1]
        passport_dict_list.append(tmp_passport)
    return passport_dict_list

def is_valid_year(st_num, low_range, high_range):
    is_valid = False
    if len(st_num) != 4:
        return is_valid
    if not (low_range <= int(st_num) <= high_range):
        return is_valid
    is_valid = True
    return is_valid

def is_valid_passport(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    is_valid = False
    passport_keys = list(passport.keys())
    if 'cid' in passport_keys:
        if len(passport_keys) == len(required_fields) + 1:
            is_valid = True
    else:
        if len(passport_keys) == len(required_fields):
            is_valid = True
    for key, val in passport.items():
        if key == 'byr' and not is_valid_year(val, 1920, 2002):
            is_valid = False
            break
        if key == 'iyr' and not is_valid_year(val, 2010, 2020):
            is_valid = False
            break
        if key == 'eyr' and not is_valid_year(val, 2020, 2030):
            is_valid = False
            break
        if key == 'hgt':
            if val[-2:] == 'cm':
                if not (150 <= int(val[:-2]) <= 193):
                    is_valid = False
            elif val[-2:] == 'in':
                if not (59 <= int(val[:-2]) <= 76):
                    is_valid = False
            else:
                is_valid = False
        if key == 'hcl':
            if (val[0] == '#' and len(val[1:]) == 6):
                try:
                    binascii.unhexlify(val[1:])
                except binascii.Error:
                    is_valid = False
                    break
            else:
                is_valid = False
        if key == 'ecl' and not val in valid_eye_colors:
            is_valid = False
            break
        if key == 'pid':
            if len(val) == 9:
                try:
                    int(val)
                except ValueError:
                    is_valid = False
            else:
                is_valid = False
    if is_valid:
        print(passport['pid'])
    return is_valid

def main():
    passports = process_passports()
    valid_passports = 0
    for passport in passports:
        if is_valid_passport(passport):
            valid_passports += 1
    print(valid_passports)

if __name__ == "__main__":
    main()
