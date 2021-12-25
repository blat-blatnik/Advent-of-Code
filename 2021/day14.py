with open('day14.txt') as file:
    lines = [line.strip() for line in file.readlines() if len(line.strip()) > 0]
    template = lines[0]
    rules = {}
    for line in lines[1:]:
        left, right = line.split(' -> ')
        rules[left] = right

def add(dict, item, count=1):
    if item not in dict:
        dict[item] = count
    else:
        dict[item] += count

def polymer_from_template(template):
    polymer = {}
    n = len(template)
    for i in range(n - 1):
        pair = template[i:i+2]
        add(polymer, pair)
    return polymer

def step(polymer, rules):
    output = {}
    for pair in polymer:
        count = polymer[pair]
        if pair in rules:
            new = rules[pair]
            add(output, pair[0] + new, count)
            add(output, new + pair[1], count)
        else:
            add(output, pair, count)
    return output

def order_counts_by_frequency(polymer):
    chars = {}
    for pair in polymer:
        count = polymer[pair]
        add(chars, pair[0], count)
        add(chars, pair[1], count)
    counts = []
    for char in chars:
        counts.append((chars[char] + 1) // 2) # Not sure why we round up, but I get a wrong answer without that so...
    return sorted(counts, reverse=True)

def answer(polymer, rules, count):
    for i in range(count):
        polymer = step(polymer, rules)
    counts = order_counts_by_frequency(polymer)
    return counts[0] - counts[-1]

polymer = polymer_from_template(template)
print('Part 1:', answer(polymer, rules, 10))
print('Part 2:', answer(polymer, rules, 40))