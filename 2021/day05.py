lines = []
with open('day05.txt') as file:
	for line in file:
		line = line.strip()
		if len(line) > 0:
			lhs, _, rhs = line.split()
			x1, y1 = (int(x) for x in lhs.split(','))
			x2, y2 = (int(x) for x in rhs.split(','))
			lines.append((x1, y1, x2, y2))

def count_overlap_points(lines, diagonals):
	w = 0
	h = 0
	for x1, y1, x2, y2 in lines:
		w = max(w, x1+1, x2+1)
		h = max(h, y1+1, y2+1)
	
	board = [[0 for _ in range(w)] for _ in range(h)]
	
	for x1, y1, x2, y2 in lines:
		xstep = +1 if x1 < x2 else 0 if x1 == x2 else -1
		ystep = +1 if y1 < y2 else 0 if y1 == y2 else -1
		if xstep != 0 and ystep != 0 and not diagonals:
			continue
		x = x1
		y = y1
		while x != x2 or y != y2:
			board[y][x] += 1
			x += xstep
			y += ystep
		board[y2][x2] += 1

	count = 0
	for y in range(h):
		for x in range(w):
			count += int(board[y][x] >= 2)
	return count

print('Part 1:', count_overlap_points(lines, diagonals=False))
print('Part 2:', count_overlap_points(lines, diagonals=True))