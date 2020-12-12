# Sample input answer is 286

class Compass(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def make_compass():
    N = Compass('N')
    E = Compass('E')
    S = Compass('S')
    W = Compass('W')
    N.right = E
    N.left = W
    E.right = S
    E.left = N
    S.right = W
    S.left = E
    W.right = N
    W.left = S
    return {'N':N, 'E':E, 'S':S, 'W':W}

class Boat(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.direction_dict = {'N':0, 'S':0, 'E':0, 'W':0}
        self.compass = make_compass()
        self.cur_facing = self.compass['E']

    def move_forward(self, distance):
        self.direction_dict[self.cur_facing.data] += distance
    
    def move_cardinal(self, direction, distance):
        self.direction_dict[direction] += distance
    
    def rotate(self, direction, degrees):
        turns = int(degrees/90)
        for _ in range(0, turns):
            if 'R' == direction:
                self.cur_facing = self.cur_facing.right
            if 'L' == direction:
                self.cur_facing = self.cur_facing.left

    def calc_man(self):
        return abs(self.direction_dict['S']-self.direction_dict['N']) + abs(self.direction_dict['E']-self.direction_dict['W'])

    def move(self):
        for direction, distance in self.instructions:
            #print(self.direction_dict)
            if direction in ['N', 'S', 'E', 'W']:
                #print(f'Moving {direction} {distance}')
                self.move_cardinal(direction, distance)
            elif direction in ['R', 'L']:
                #print(f'Rotating {direction} {distance}')
                self.rotate(direction, distance)
            elif direction in ['F']:
                #print(f'Moving forward')
                self.move_forward(distance)
        return self.calc_man()

class Boat2(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.direction_dict = {'N':0, 'S':0, 'E':0, 'W':0}
        self.compass = make_compass()
        # self.cur_facing = self.compass['E']
        self.waypoint = {'E':10, 'N':1, 'S':0, 'W':0}

    def move_forward(self, distance):
        for key, val in self.waypoint.items():
            self.direction_dict[key] += distance*val
    
    def move_waypoint_cardinal(self, direction, distance):
        self.waypoint[direction] += distance
    
    def rotate(self, direction, degrees):
        turns = int(degrees/90)
        new_waypoint = {}
        for _ in range(0, turns):
            for key, _ in self.waypoint.items():
                if direction == 'R':
                    new_waypoint[self.compass[key].right.data] = self.waypoint[key]
                elif direction == 'L':
                    new_waypoint[self.compass[key].left.data] = self.waypoint[key]
            self.waypoint = new_waypoint
            new_waypoint = {}

    def calc_man(self):
        return abs(self.direction_dict['S']-self.direction_dict['N']) + abs(self.direction_dict['E']-self.direction_dict['W'])

    def move(self):
        for direction, distance in self.instructions:
            # print('move dict', end='')
            # print(self.direction_dict)
            # print('waypoint dict', end='')
            # print(self.waypoint)
            if direction in ['N', 'S', 'E', 'W']:
                #print(f'Moving {direction} {distance}')
                self.move_waypoint_cardinal(direction, distance)
            elif direction in ['R', 'L']:
                #print(f'Rotating {direction} {distance}')
                self.rotate(direction, distance)
            elif direction in ['F']:
                #print(f'Moving forward')
                self.move_forward(distance)
        return self.calc_man()

def main(path='twelve.input.sample'):
    with open(path, 'r') as f:
        instructions = [(tmp.replace('\n', '')[0], int(tmp.replace('\n', '')[1:])) for tmp in f.readlines()]
    B = Boat2(instructions)
    print(B.move())

if __name__ == "__main__":
    main('twelve.input')
    # main('twelve.input.sample')