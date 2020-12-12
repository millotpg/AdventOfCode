# sample solution is 4
import json

def process_rules(data):
    rules_dict = {}
    for rule in data:
        rule = rule.replace('\n', '').replace('.', '').replace('bags', 'bag')
        rule_container = rule.split('contain')[0][:-1]
        if rule.split('contain')[1] == ' no other bag':
            rule_contains = None
        else:
            rule_contains = [(int(tmp1.split(' ')[0]), ' '.join(tmp1.split(' ')[1:])) for tmp1 in [tmp[1:] for tmp in rule.split('contain')[1].split(',')]]
        rules_dict[rule_container] = rule_contains
    return rules_dict

def traverse_rules(rules_dict, desired_bag, found_bags):
    for key, values in rules_dict.items():
        if values and desired_bag in [tmp[1] for tmp in values]:
            found_bags.append(key)
            traverse_rules(rules_dict, key, found_bags)
    return found_bags

def count_bags(rules_dict, desired_bag, bag_count):
    print('counting bags for ' + desired_bag)
    bag_list = rules_dict[desired_bag]
    cur_total = 1
    if not bag_list:
        return 1
    for total_bags, bag_style in bag_list:
        cur_total += total_bags * count_bags(rules_dict, bag_style, bag_count)
    return cur_total

def main():
    desired_bag = 'shiny gold bag'
    with open('seven.input', 'r') as f:
        data = f.readlines()
    rules_dict = process_rules(data)
    x = traverse_rules(rules_dict, desired_bag, [])
    print(len(set(x)))
    print(count_bags(rules_dict, desired_bag, 0) - 1)

if __name__ == "__main__":
    main()
