dots = []
folds = []
with open('day13.txt') as file:
	doing_folds = False
	for line in file:
		line = line.strip()
		if len(line) == 0 and len(folds) == 0:
			doing_folds = True
		elif len(line) > 0:
			if doing_folds:
				_, _, fold = line.split()
				axis, pos = fold.split('=')
				pos = int(pos)
				folds.append([axis, pos])
			else:
				dots.append([int(x) for x in line.split(',')])

w = 0
h = 0
for x, y in dots:
	w = max(w, x + 1)
	h = max(h, y + 1)

def make_board(w, h):
	return [['.' for x in range(w)] for y in range(h)]

board = make_board(w, h)
for x, y in dots:
	board[y][x] = '#'

def do_fold(board, fold):
	h = len(board)
	w = len(board[0])
	axis, pos = fold

	if axis == 'x':
		lw = pos
		rw = w - pos - 1
		folded_h = h
		folded_w = max(lw, rw)
		part1 = make_board(folded_w, folded_h)
		part2 = make_board(folded_w, folded_h)
		for y in range(folded_h):
			for x in range(lw):
				offset = max(0, folded_w - lw)
				part1[y][offset + x] = board[y][x]
			for x in range(rw):
				offset = max(0, folded_w - rw)
				part2[y][offset + x] = board[y][w - x - 1]
	else:
		th = pos
		bh = h - pos - 1
		folded_h = max(th, bh)
		folded_w = w
		part1 = make_board(folded_w, folded_h)
		part2 = make_board(folded_w, folded_h)
		for x in range(folded_w):
			for y in range(th):
				offset = max(0, folded_h - th)
				part1[offset + y][x] = board[y][x]
			for y in range(bh):
				offset = max(0, folded_h - bh)
				part2[offset + y][x] = board[h - y - 1][x]

	folded = make_board(folded_w, folded_h)
	for y in range(folded_h):
		for x in range(folded_w):
			if part1[y][x] == '#' or part2[y][x] == '#':
				folded[y][x] = '#'
	return folded

def count_dots(board):
	count = 0
	for row in board:
		for pos in row:
			if pos == '#':
				count += 1
	return count

print('Part 1:', count_dots(do_fold(board, folds[0])))
print('Part 2:')
for fold in folds:
	board = do_fold(board, fold)
for row in board:
	print(''.join(row))