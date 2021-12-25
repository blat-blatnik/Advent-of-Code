with open('day17.txt') as file:
    line = file.readline().strip()
    _, _, x_range, y_range = line.split()
    x_range = x_range.split('=')[1].removesuffix(',')
    y_range = y_range.split('=')[1].removesuffix(',')
    x_min, x_max = [int(x) for x in x_range.split('..')]
    y_min, y_max = [int(y) for y in y_range.split('..')]

# This whole solution assumes the target is in the bottom-right quadrant. 
assert x_min > 0
assert y_max < 0

def simulate_vy(vy, y_min, y_max):
    y = 0
    max_y = 0
    while y > y_min:
        y += vy
        vy -= 1
        max_y = max(y, max_y)
        if y >= y_min and y <= y_max:
            return True, max_y
    return False, max_y

def part1(y_min, y_max):
    best_height = 0
    for vy in range(-y_min + 1, y_min - 1, -1):
        hit, max_y = simulate_vy(vy, y_min, y_max)
        if hit and max_y > best_height:
            best_height = max_y
    return best_height

def simulate(vx, vy, x_min, x_max, y_min, y_max):
    x = 0
    y = 0
    while x <= x_max and y >= y_min:
        if x >= x_min and y <= y_max:
            return True
        x += vx
        y += vy
        vx = max(0, vx - 1)
        vy -= 1
    return False

def part2(x_min, x_max, y_min, y_max):
    count = 0
    for vx in range(0, x_max + 1):
        for vy in range(-y_min + 1, y_min - 1, -1):
            if simulate(vx, vy, x_min, x_max, y_min, y_max):
                count += 1
    return count

print('Part 1:', part1(y_min, y_max))
print('Part 2:', part2(x_min, x_max, y_min, y_max))