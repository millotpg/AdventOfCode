
def is_valid_num(preamble, cur_check_num):
    for num in preamble:
        if cur_check_num - num in preamble:
            return True
    return False

def find_contiguous_sum(data, cur_index, cur_check_num):
    cur_sum = 0
    cur_sum_list = []
    for i in range(0, cur_index):
        cur_sum = data[i]
        cur_sum_list.append(data[i])
        for k in range(i+1, cur_index):
            # print(cur_sum_list)
            cur_sum_list.append(data[k])
            cur_sum += data[k]
            if cur_sum == cur_check_num:
                return min(cur_sum_list) + max(cur_sum_list)
            if cur_sum > cur_check_num:
                cur_sum = 0
                cur_sum_list = []
                break

def find_incorrect_item(data, preamble_len):
    cur_index = 0
    cur_preamble = data[:preamble_len]
    cur_check_num = data[preamble_len]
    while True:
        if not is_valid_num(cur_preamble, cur_check_num):
            find_contiguous_sum(data, cur_index, cur_check_num)
            return cur_check_num, find_contiguous_sum(data, cur_index, cur_check_num)
        cur_index += 1
        cur_preamble = data[cur_index:cur_index+preamble_len]
        cur_check_num = data[cur_index+preamble_len]

def main():
    with open('nine.input', 'r') as f:
        data = [int(tmp) for tmp in f.readlines()]
    preamble_len = 25
    print(find_incorrect_item(data, preamble_len))

if __name__ == "__main__":
    main()