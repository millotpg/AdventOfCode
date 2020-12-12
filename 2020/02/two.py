

def find_valid_passowrds():
    with open('two.input', 'r') as f:
        data = f.readlines()
    data = [(x.replace('\n', '').split(':')) for x in data]
    incorrect_password = 0
    for policy, passwd in data:
        occ_range, tok = policy.split(' ')
        low_occ_val, high_occ_val = occ_range.split('-')
        low_occ_val = int(low_occ_val)
        high_occ_val = int(high_occ_val)
        tok_count = passwd.count(tok)
        # print(f'Low_occ: {low_occ_val} | tok_count: {tok_count} | high_occ_val: {high_occ_val}')
        if tok_count < low_occ_val or tok_count > high_occ_val:
            incorrect_password += 1
    print(len(data) - incorrect_password)

def find_new_valid_passwords():
    with open('two.input', 'r') as f:
        data = f.readlines()
    data = [(x.replace('\n', '').split(':')) for x in data]
    correct_password = 0
    match = 0
    for policy, passwd in data:
        occ_range, tok = policy.split(' ')
        low_index, high_index = occ_range.split('-')
        low_index = int(low_index)
        high_index = int(high_index)
        passwd = passwd.replace(' ', '')
        if passwd[low_index-1] == tok:
            match += 1
        if passwd[high_index-1] == tok:
            match += 1
        if match == 1:
            correct_password += 1
            print(f'passwd: {passwd} | policy: {policy} | low-high {low_index} {high_index} |passowd[low,high]: {passwd[low_index-1]}, {passwd[high_index-1]}| match: True')
        match = 0
    print(correct_password)


if __name__ == "__main__":
    find_valid_passowrds()
    find_new_valid_passwords()