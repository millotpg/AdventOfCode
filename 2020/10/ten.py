# [1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49]
import time
def can_remove(data, index):
    if 3 >= data[index+1] - data[index-1]:
        return True
    return False

def count_arrangements(data, cur_start, arr_count):
    for i in range(cur_start, len(data)-1):
        if can_remove(data, i):
            arr_count =  count_arrangements(data[:i] + data[i+1:], i, arr_count+1)
    return arr_count

def calculate_jolt_differences(data):
    differences = []
    for i in range(1, len(data)):
        differences.append(data[i]-data[i-1])
    differences.append(3)
    differences.append(1)
    differences_dict = {}
    for i in differences:
        try:
            differences_dict[i] += 1
        except KeyError:
            differences_dict[i] = 1
    print(differences_dict[1] * differences_dict[3])

def split_on_difference_three(data):
    lists = []
    start = 0
    end = 0
    for i in range(1, len(data)-1):
        if data[i] - data[i-1] == 3:
            lists.append(data[start:i])
            start = i
    lists.append(data[start:])
    return lists

def main():
    start_time = time.time()
    with open('ten.input', 'r') as f:
        data = [int(tmp) for tmp in f.readlines()]
    # data = [1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 17, 18, 19]
    data.sort()
    data.insert(0, 0)
    x = split_on_difference_three(data)
    product_list = []
    cur_prod = 1
    for tmp in x:
        product_list.append(count_arrangements(tmp, 1, 1))
    for itm in product_list:
        cur_prod = cur_prod * itm
    print(cur_prod)
    print()
    print(time.time() - start_time)
    #calculate_jolt_differences(data)

if __name__ == "__main__":
    main()