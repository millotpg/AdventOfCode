
def part_one(group_data):
    cur_total_yeses = 0
    for tmp in group_data:
        cur_total_yeses += len(list(set(tmp.replace('\n', ''))))
    print(cur_total_yeses)

def part_two(group_data):
    group_dict = {}
    total_yeses = 0
    for group in group_data:
        group_size = len(group.split('\n'))
        for answer in group.replace('\n', ''):
            try:
                group_dict[answer] += 1
            except KeyError:
                group_dict[answer] = 1
        for key, val in group_dict.items():
            if val == group_size:
                total_yeses += 1
        group_dict = {}
    print(total_yeses)

def main():
    with open('six.input', 'r') as f:
        data = f.read()
    group_data = data.split('\n\n')
    part_one(group_data)
    part_two(group_data)

if __name__ == "__main__":
    main()