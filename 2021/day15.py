cells = []
with open('day15.txt') as file:
    for line in file:
        line = line.strip()
        if len(line) > 0:
            cells.append([int(x) for x in line])

def minimum_risk(cells):
    import heapq
    h = len(cells)
    w = len(cells[0])
    visited = [[False for x in row] for row in cells]
    visited[0][0] = True
    queue = [(0, 0, 0)]
    while len(queue) > 0:
        risk, x, y = heapq.heappop(queue)
        if x == w - 1 and y == h - 1:
            return risk
        for dx, dy in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < w and ny >= 0 and ny < h and not visited[ny][nx]:
                visited[ny][nx] = True
                heapq.heappush(queue, (risk + cells[ny][nx], nx, ny))

def expand(cells):
    h = len(cells)
    w = len(cells[0])
    expanded_w = 5 * w
    expanded_h = 5 * h
    expanded_cells = [[0 for x in range(expanded_w)] for y in range(expanded_h)]
    for ry in range(5):
        for rx in range(5):
            for ly in range(h):
                for lx in range(w):
                    y = h * ry + ly
                    x = w * rx + lx
                    expanded_cells[y][x] = 1 + (cells[ly][lx] - 1 + rx + ry) % 9
    return expanded_cells 

print('Part 1:', minimum_risk(cells))
print('Part 2:', minimum_risk(expand(cells)))