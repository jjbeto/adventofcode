import re

from aocd import get_data

raw = get_data(day=7, year=2020)

lines = raw.split('.\n')
re_bag = '([a-z ]+) bags? contain [\\w ]+'
re_list = '(\\d+)[ ]?([ a-z]+) bags?'

bags_all = set()
bags = {}
for line in lines:
    main_bag = re.findall(re_bag, line)[0]
    list_of_bags = [pair[1] for pair in re.findall(re_list, line)]
    bags[main_bag] = list_of_bags
    bags_all.update(list_of_bags + [main_bag])


def fit_iterator(bag, target):
    if bag in bags[target]:
        return 1
    for next_target in bags[target]:
        contains_bag = fit_iterator(bag, next_target)
        if contains_bag:
            return contains_bag
    return 0


def fit(bag):
    count = 0
    for each in bags_all:
        count += fit_iterator(bag, each)
    return count


print(f'Answer 1: {fit("shiny gold")}')

bags_complete = {}
for line in lines:
    bags_complete[re.findall(re_bag, line)[0]] = [pair for pair in re.findall(re_list, line)]


def count_iterator(bag):
    return sum([count_iterator(pair[1]) * int(pair[0]) + int(pair[0]) for pair in bags_complete[bag]])


print(f'Answer 2: {count_iterator("shiny gold")}')
