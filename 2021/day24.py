# This will literally take 2+ hours to run.
# It will still work - but if you just want an answer, use day24.c instead, which only takes 5 minutes or so.

with open('day24.txt') as file:
	lines = [line.strip() for line in file]

def add_state(states, regs, new_highest, new_lowest):
	state = (regs['w'], regs['x'], regs['y'], regs['z'])
	if state in states:
		highest, lowest = states[state]
		highest = max(highest, new_highest)
		lowest = min(lowest, new_lowest)
		states[state] = (highest, lowest)
	else:
		states[state] = (new_highest, new_lowest)

def execute_branching(instructions):
	states = { (0, 0, 0, 0):(0, 0) }
	for line, instruction in enumerate(instructions):
		next_states = {}
		slots = instruction.split()
		opcode = slots[0]
		a = slots[1]
		if opcode == 'inp':
			for state, (highest, lowest) in states.items():
				reg = { 'w':state[0], 'x':state[1], 'y':state[2], 'z':state[3] }
				for i in range(1, 10):
					reg[a] = i
					add_state(next_states, reg, 10 * highest + i, 10 * lowest + i)
		else:
			for state, (highest, lowest) in states.items():
				reg = { 'w':state[0], 'x':state[1], 'y':state[2], 'z':state[3] }
				b = slots[2]
				if b in 'wxyz':
					b = reg[b]
				else:
					b = int(b)
				if opcode == 'add':
					reg[a] += b
				elif opcode == 'mul':
					reg[a] *= b
				elif opcode == 'div':
					reg[a] //= b
				elif opcode == 'mod':
					reg[a] %= b
				elif opcode == 'eql':
					reg[a] = int(reg[a] == b)
				add_state(next_states, reg, highest, lowest)
		states = next_states
		print(f'line {line + 1}: {len(states)} states')
	return states

states = execute_branching(lines)
part1 = 0
part2 = 10**15 - 1
for state, highest_input in states.items():
	if state[3] == 0:
		part1 = max(part1, highest_input)
		part2 = min(part2, highest_input)

print('Part 1:', part1)
print('Part 2:', part2)