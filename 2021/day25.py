cells = []
with open('day25.txt') as file:
	for line in file:
		line = line.strip()
		if len(line) > 0:
			cells.append(line)

def step(cells):
	h = len(cells)
	w = len(cells[0])
	next = [['.' for _ in row] for row in cells]
	moved = False
	for y in range(h):
		for x in range(w):
			if cells[y][x] == '>':
				tx = (x + 1) % w
				if cells[y][tx] == '.':
					next[y][tx] = '>'
					moved = True
				else:
					next[y][x] = '>'
			elif cells[y][x] == 'v':
				next[y][x] = 'v'
	cells = next
	next = [['.' for _ in row] for row in cells]
	for y in range(h):
		for x in range(w):
			if cells[y][x] == 'v':
				ty = (y + 1) % h
				if cells[ty][x] == '.':
					next[ty][x] = 'v'
					moved = True
				else:
					next[y][x] = 'v'
			elif cells[y][x] == '>':
				next[y][x] = '>'
	return next, moved

def part1(cells):
	i = 0
	while True:
		i += 1
		cells, moved = step(cells)
		if not moved:
			break
	return i

print('Part 1:', part1(cells))
# There is no part 2 :)