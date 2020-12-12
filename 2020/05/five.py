
def convert_to_id(seat_str):
    return 8 * int(seat_str[:-3].replace('B', '1').replace('F', '0'), 2) + int(seat_str[-3:].replace('R', '1').replace('L', '0'), 2)

def main():
    with open('five.input', 'r') as f:
        data = [convert_to_id(tmp.replace('\n', '')) for tmp in f.readlines()]
    print(max(data))
    sorted_data = sorted(data)
    for i in range(0, len(sorted_data)-1):
        if sorted_data[i] + 1 == sorted_data[i + 1]:
            pass
        else:
            print(sorted_data[i] + 1)

if __name__ == "__main__":
    main()