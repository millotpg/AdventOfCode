

def make_move(cur_x, cur_y, max_x, slope_tuple):
    cur_x = cur_x + slope_tuple[0]
    cur_y = cur_y + slope_tuple[1]
    if cur_x > max_x:
        cur_x = cur_x - max_x - 1
    return cur_x, cur_y

def main():
    with open('three.input', 'r') as f:
        data = [x.replace('\n', '') for x in f.readlines()]
    max_y = len(data) - 1
    max_x = len(data[0]) - 1
    slope_tuple_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_count_lst = []
    tree_count = 0
    cur_x = 0
    cur_y = 0
    for slope_tuple in slope_tuple_list:
        print(slope_tuple)
        while True:
            print(f"cur_x: {cur_x} | cur_y: {cur_y} | cur_pos: {data[cur_y][cur_x]}")
            if data[cur_y][cur_x] == '#':
                tree_count += 1
            if cur_y == max_y:
                break
            cur_x, cur_y = make_move(cur_x, cur_y, max_x, slope_tuple)
        tree_count_lst.append(tree_count)
        tree_count = 0
        cur_x = 0
        cur_y = 0
    prod = 1
    print(tree_count_lst)
    for tmp in tree_count_lst:
        prod = prod * tmp
    print(prod)


if __name__ == "__main__":
    main()