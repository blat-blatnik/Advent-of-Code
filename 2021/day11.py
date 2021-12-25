energy = []
with open('day11.txt') as file:
    for line in file:
        line = line.strip()
        if len(line) > 0:
            energy.append([int(char) for char in line])

def step(energy):
    h = len(energy)
    w = len(energy[0])

    def bump(x, y):
        energy[y][x] += 1
        if energy[y][x] == 10:
            flashes = 1
            for yn in range(y - 1, y + 2):
                for xn in range(x - 1, x + 2):
                    if xn >= 0 and xn < w and yn >= 0 and yn < h:
                        flashes += bump(xn, yn)
            return flashes
        else:
            return 0

    flashes = 0
    for y in range(h):
        for x in range(w):
            flashes += bump(x, y)

    all_flash = True
    for y in range(h):
        for x in range(w):
            if energy[y][x] >= 10:
                energy[y][x] = 0
            else:
                all_flash = False

    return flashes, all_flash

def part1(energy):
    energy = [row.copy() for row in energy]
    flashes = 0
    for i in range(100):
        inc, _ = step(energy)
        flashes += inc
    return flashes

def part2(energy):
    energy = [row.copy() for row in energy]
    for i in range(1000000):
        _, all_flash = step(energy)
        if all_flash:
            return i + 1

print('Part 1:', part1(energy))
print('Part 2:', part2(energy))