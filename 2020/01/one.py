
def find_two():
    with open('one.input', 'r') as f:
        data = f.readlines()
    data = [int(x) for x in data]
    for x in data:
        for y in data:
            if x + y == 2020:
                print(x*y)
                return
    print('Sum not found')


def find_three():
    with open('one.input', 'r') as f:
        data = f.readlines()
    data = [int(x) for x in data]
    for x in data:
        for y in data:
            for z in data:
                if x + y + z == 2020:
                    print(x*y*z)


if __name__ == "__main__":
    find_two()
    find_three()