
def count_occupied_adjacent_seats(row, col, data):
    occupied_seats = 0
    max_col = len(data[0])-1
    max_row = len(data) - 1
    min_row = 0
    min_col = 0
    adjacent_coords = [(row-1, col-1), 
                       (row-1, col),
                       (row, col-1),
                       (row+1, col+1),
                       (row+1, col),
                       (row, col+1),
                       (row-1, col+1),
                       (row+1, col-1)]
    valid_coords = []
    for coord_row, coord_col in adjacent_coords:
        if coord_row < min_row or coord_col < min_col or coord_col > max_col or coord_row > max_row:
            continue
        valid_coords.append((coord_row, coord_col))
    for coord_row, coord_col in valid_coords:
        if '#' == data[coord_row][coord_col]:
            occupied_seats += 1
    return occupied_seats

def count_seats_in_sight(row, col, data):
    occupied_seats = 0
    max_col = len(data[0])
    max_row = len(data)
    line_of_sight = {}
    try:
        line_of_sight['right'] = data[row][col+1:]
    except IndexError:
        line_of_sight['right'] = ''
    line_of_sight['left'] = data[row][:col][::-1]
    try:
        line_of_sight['down'] = ''.join([tmp[col] for tmp in data])[row+1:]
    except IndexError:
        line_of_sight['down'] = ''
    line_of_sight['up'] = ''.join([tmp[col] for tmp in data])[:row][::-1]
    line_of_sight['up-right'] = ''
    line_of_sight['up-left'] = ''
    line_of_sight['down-right'] = ''
    line_of_sight['down-left'] = ''
    for index in range(1, max(max_row, max_col)):
        if (row - index >= 0) and (col - index >= 0):
            line_of_sight['up-left'] += data[row - index][col - index]
        if (row + index < max_row) and (col + index < max_col):
            line_of_sight['down-right'] += data[row + index][col + index]
        if (row - index >= 0) and (col + index < max_col):
            line_of_sight['up-right'] += data[row - index][col + index]
        if (row + index < max_row) and (col - index >= 0):
            line_of_sight['down-left'] += data[row + index][col - index]
    for _, val in line_of_sight.items():
        val = val.replace('.', '')
        if val and val[0] == '#':
            occupied_seats += 1
    return occupied_seats

def file_people_in(data):
    people_moved = False
    shuffle_move = []
    max_col = len(data[0])
    max_row = len(data)
    for cur_row in range(0, max_row):
        cur_row_lst = []
        for cur_col in range(0, max_col):
            if 'L' == data[cur_row][cur_col]:
                if 0 == count_seats_in_sight(cur_row, cur_col, data):
                    people_moved = True
                    cur_row_lst.append('#')
                else:
                    cur_row_lst.append('L')
            elif '#' == data[cur_row][cur_col]:
                if 5 <= count_seats_in_sight(cur_row, cur_col, data):
                    people_moved = True
                    cur_row_lst.append('L')
                else:
                    cur_row_lst.append('#')
            else:
                cur_row_lst.append(data[cur_row][cur_col])
        shuffle_move.append(''.join(cur_row_lst))
        cur_row = []
    return people_moved, shuffle_move

def people_watch(data):
    shuffle_count = 0
    people_still_moving = True
    while people_still_moving:
        print_data(data)
        shuffle_count += 1
        people_still_moving, data = file_people_in(data)
    print(sum([tmp.count('#') for tmp in data]))

def print_data(data):
    for i in data:
        print(i)
    print()

def read_in_data(path):
    with open(path, 'r') as f:
        data = [tmp.replace('\n', '') for tmp in f.readlines()]
    return data

def main():
    data = read_in_data('eleven.input')
    #print(count_seats_in_sight(2, 4, data))
    people_watch(data)

if __name__ == "__main__":
    main()