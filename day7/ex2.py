# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.

# In this example, a single shiny gold bag must contain 126 other bags.

# 2 + (2^2) + (2^3) + (2^4) + (2^5) + (2^6)
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

def bags_inside(bag_color, rules):
    return 1 + sum(count * bags_inside(name, rules) for count, name in rules[bag_color])


def bags_in_shiny_gold(rules):
    print('Individual bags inside single shiny gold bag',bags_inside("shiny gold", rules) - 1)

f = open('input.txt', 'r')
data = f.read().splitlines()
rules = dict([ruleparser(line) for line in data])
bags_in_shiny_gold(rules)
