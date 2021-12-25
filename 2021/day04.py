with open('day04.txt') as file:
	lines = file.readlines()
	lines.append('')

numbers = [int(num) for num in lines[0].split(',')]

lines = lines[2:]
num_boards = len(lines) // (5+1)
	
boards = []
for i in range(num_boards):
	board = []
	board_lines = lines[(i)*(5+1) : (i+1)*(5+1)]
	for board_line in board_lines[:5]:
		board.append([int(num) for num in board_line.split()])
	boards.append(board)

marks = []
for board in boards:
	marks.append([[0,0,0,0,0] for i in range(5)])

def check_board(mark):
	for y in range(5):
		row_complete = True
		for x in range(5):
			row_complete &= (mark[y][x] == 1)
		if row_complete:
			return True
	for x in range(5):
		col_complete = True
		for y in range(5):
			col_complete &= (mark[y][x] == 1)
		if col_complete:
			return True
	return False

def winning_board_index(marks):
	for i, mark in enumerate(marks):
		if check_board(mark):
			return i
	return -1

def update_marks(boards, marks, number):
	for board, mark in zip(boards, marks):
		for y in range(5):
			for x in range(5):
				if board[y][x] == number:
					mark[y][x] = 1

def score_board(board, mark):
	score = 0
	for y in range(5):
		for x in range(5):
			if mark[y][x] == 0:
				score += board[y][x]
	return score

winning_board = None
winning_mark = None
winning_number = -1
losing_board = None
losing_mark = None
losing_number = -1
for number in numbers:
	update_marks(boards, marks, number)
	while True:
		index = winning_board_index(marks)
		if index == -1:
			break
		else:
			if winning_board == None:
				winning_board = boards[index]
				winning_mark = marks[index]
				winning_number = number
			else:
				losing_board = boards[index]
				losing_mark = marks[index]
				losing_number = number
			del boards[index]
			del marks[index]

print('Part 1:', winning_number * score_board(winning_board, winning_mark))
print('Part 2:', losing_number * score_board(losing_board, losing_mark))

