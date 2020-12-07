# A bright white bag, which can hold your shiny gold bag directly.
# A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
# A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

import re
import time

bagexp = re.compile("^(\d+) ([a-z ]+) bags?\.?$")
def count_bags(bag):
    count, description = bagexp.match(bag).groups()
    return (int(count), description)


def ruleparser(rule):
    main_bag, contents = rule.split(" bags contain ")
    if contents == "no other bags.":
        return main_bag, []
    return main_bag, [count_bags(bag) for bag in contents.split(', ')]

def contains_gold(bag_name, rules):
    if bag_name == "shiny gold":
        return True
    return any(contains_gold(name, rules) for _, name in rules[bag_name])

def at_least_one_shiny_goldbag(rules):
    print('Total number of bag colors that contain at least one shiny gold bag =',sum((contains_gold(name, rules) and 1 or 0) for name in rules if name != "shiny gold"))

f = open('input.txt', 'r')
data = f.read().splitlines()
rules = dict([ruleparser(line) for line in data])
at_least_one_shiny_goldbag(rules)
