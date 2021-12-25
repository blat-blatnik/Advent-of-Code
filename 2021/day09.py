heightmap = []
with open('day09.txt') as file:
    for line in file:
        line = line.strip()
        if len(line) > 0:
            heightmap.append([int(char) for char in line])

def get_neighbors(heightmap, x, y):
    h = len(heightmap)
    w = len(heightmap[0])
    neighbors = []
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if nx >= 0 and ny >= 0 and nx < w and ny < h:
            neighbors.append((nx, ny))
    return neighbors

def find_low_points(heightmap):
    h = len(heightmap)
    w = len(heightmap[0])
    low_points = []
    for y in range(h):
        for x in range(w):
            height = heightmap[y][x]
            neighbor_heights = [heightmap[ny][nx] for nx, ny in get_neighbors(heightmap, x, y)]
            if all(height < neighbor for neighbor in neighbor_heights):
                low_points.append((x, y))
    return low_points

def basin(heightmap, processed, x, y):
    if processed[y][x]:
        return 0
    if heightmap[y][x] == 9:
        return 0
    processed[y][x] = True
    return 1 + sum(basin(heightmap, processed, nx, ny) for nx, ny in get_neighbors(heightmap, x, y))

low_points = find_low_points(heightmap)

h = len(heightmap)
w = len(heightmap[0])
processed = [[False for x in range(w)] for y in range(h)]
basin_sizes = sorted([basin(heightmap, processed, x, y) for x, y in low_points], reverse=True)

part1 = sum(1 + heightmap[y][x] for x, y in low_points)
part2 = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
print('Part 1:', part1)
print('Part 2:', part2)