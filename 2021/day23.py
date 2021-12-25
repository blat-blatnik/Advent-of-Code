with open('day23.txt') as file:
	lines = file.read().splitlines()

TARGET_ROOMS = {
	'A': 2,
	'B': 4,
	'C': 6,
	'D': 8,
}
MOVE_COSTS = {
	'A': 1,
	'B': 10,
	'C': 100,
	'D': 1000,
}
ROOM_POSITIONS = set(TARGET_ROOMS.values())

def parse(lines):
	h = len(lines)
	room_size = h - 3
	rooms = [[] for _ in range(4)]
	for i, room in enumerate(rooms):
		x = 3 + 2 * i
		for y in range(2, 2 + room_size):
			room.append(lines[y][x])
	rooms = [''.join(room) for room in rooms]
	return ['.', '.', rooms[0], '.', rooms[1], '.', rooms[2], '.', rooms[3], '.', '.']

def is_path_clear(board, start_pos, end_pos):
	a = min(start_pos, end_pos)
	b = max(start_pos, end_pos)
	for pos in range(a, b + 1):
		if pos == start_pos:
			continue
		if pos in ROOM_POSITIONS:
			continue
		if board[pos] != '.':
			return False
	return True

def room_contains_only_goal_chars(board, piece, dest_pos):
	in_room = board[dest_pos]
	return len(in_room) == in_room.count('.') + in_room.count(piece) 

def first_char_in_room(room):
	for c in room:
		if c != '.':
			return c

def possible_moves(board, pos):
	piece = board[pos]
	if pos not in ROOM_POSITIONS:
		if is_path_clear(board, pos, TARGET_ROOMS[piece]) and room_contains_only_goal_chars(board, piece, TARGET_ROOMS[piece]):
			return [TARGET_ROOMS[piece]]
		return []

	moving_char = first_char_in_room(piece)
	if pos == TARGET_ROOMS[moving_char] and room_contains_only_goal_chars(board, moving_char, pos):
		return []

	moves = []
	for dest in range(len(board)):
		if dest == pos:
			continue
		if dest in ROOM_POSITIONS and TARGET_ROOMS[moving_char] != dest:
			continue
		if TARGET_ROOMS[moving_char] == dest:
			if not room_contains_only_goal_chars(board, moving_char, dest):
				continue
		if is_path_clear(board, pos, dest):
			moves.append(dest)
	return moves

def add_to_room(char, room):
	room = list(room)
	dist = room.count('.')
	assert dist != 0
	room[dist - 1] = char
	return ''.join(room), dist

def move(board, pos, dest):
	new_board = board.copy()
	dist = 0
	moving_char = first_char_in_room(board[pos])
	if len(board[pos]) == 1:
		new_board[pos] = '.'
	else:
		new_room = ''
		found = False
		for c in board[pos]:
			if c == '.':
				dist += 1
				new_room += c
			elif not found:
				new_room += '.'
				dist += 1
				found = True
			else:
				new_room += c
		new_board[pos] = new_room
	
	dist += abs(pos - dest)

	if len(board[dest]) == 1:
		new_board[dest] = moving_char
		return new_board, dist * MOVE_COSTS[moving_char]
	else:
		new_board[dest], in_room_dist = add_to_room(moving_char, board[dest])
		dist += in_room_dist
		return new_board, dist * MOVE_COSTS[moving_char]

def solve(lines):
	board = parse(lines)
	room_size = len(board[2])
	states = { tuple(board):0 }
	queue = [board]
	while queue:
		board = queue.pop()
		for pos, piece in enumerate(board):
			if first_char_in_room(piece) is None:
				continue
			dests = possible_moves(board, pos)
			for dest in dests:
				new_board, move_cost = move(board, pos, dest)
				new_cost = states[tuple(board)] + move_cost
				cost = states.get(tuple(new_board), 999999999)
				if new_cost < cost:
					states[tuple(new_board)] = new_cost
					queue.append(new_board)
	return states[('.', '.', 'A'*room_size, '.', 'B'*room_size, '.', 'C'*room_size, '.', 'D'*room_size, '.', '.')]

print('Part 1:', solve(lines))
print('Part 2:', solve(lines[:-2] + ['  #D#C#B#A#', '  #D#B#A#C#'] + lines[-2:]))