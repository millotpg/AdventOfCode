
def greatest_common_factor(nums):
    factor_dict = {}
    for i in nums:
        factor_dict[i] = []
        for k in range(1, i // 2):
            if i % k == 0:
                factor_dict[i].append(k)
    common_factors = []
    for factor in factor_dict[nums[0]]:
        for _, val in factor_dict.items():
            if factor in val:
                common_factors.append(factor)
    return max(common_factors)

def least_common_multiple(nums):
    prod = 1
    for num in nums:
        prod = prod * num
    return prod // greatest_common_factor(nums)

def is_valid(mods_dict, num):
    for key, val in mods_dict.items():
        if num % key != val['key']:
            return False
    return True

def part_two(bus_ids):
    # bus_ids = [int(tmp) for tmp in bus_ids if not tmp == 'x']
    # bus_ids.sort()
    mod_dict = {}
    thiccest_boi = max([int(tmp) for tmp in bus_ids if not tmp == 'x'])
    index_of_thiccest_boi = bus_ids.index(str(thiccest_boi))

    for offset in range(0, len(bus_ids)):
        if bus_ids[offset] != 'x':
            if offset < index_of_thiccest_boi:
                mod_dict[int(bus_ids[offset])] = {'key':index_of_thiccest_boi - offset}
            elif offset == index_of_thiccest_boi:
                mod_dict[int(bus_ids[offset])] = {'key': 0}
            else:
                mod_dict[int(bus_ids[offset])] = {'key':int(bus_ids[offset]) - (offset - index_of_thiccest_boi)}

    # Generate a list of multiples...kind of a stab in the dark at a search space
    lcm = least_common_multiple([int(tmp) for tmp in bus_ids if not tmp == 'x'])
    cur_check = 0
    while cur_check < lcm:
        if is_valid(mod_dict, cur_check):
            print(cur_check - index_of_thiccest_boi)
        cur_check += thiccest_boi

# Sample answer = 295 (bus id * minutes to wait)
def part_one(target_departure, bus_ids):
    bus_ids = [int(tmp) for tmp in bus_ids if not tmp == 'x']
    bus_ids.sort()
    target_departure = int(target_departure)
    bus_schedule = {}
    for bus_id in bus_ids:
        bus_schedule[bus_id] = []
        bus_schedule[bus_id] = (((target_departure // bus_id)+1) * bus_id) - target_departure
    min_key = min(bus_schedule, key=bus_schedule.get)
    print(min_key * bus_schedule[min_key])

def main(path='thirteen.input.sample'):
    with open(path, 'r') as f:
        data = [tmp.replace('\n', '') for tmp in f.readlines()]
    target_departure, bus_ids = data[0], data[1].split(',')
    # part_one(target_departure, bus_ids)
    part_two(bus_ids)

if __name__ == "__main__":
    #main()
    main('thirteen.input')
