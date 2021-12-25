bits = []
with open('day03.txt') as file:
	for line in file:
		line = line.strip()
		if len(line) > 0:
			bits.append([int(char) for char in line])

def most_common_bit(bits, x):
	n0 = 0
	n1 = 0
	for y in range(len(bits)):
		n0 += int(bits[y][x] == 0)
		n1 += int(bits[y][x] == 1)
	return int(n1 >= n0)

def find_power_consumption(bits):
	gamma = 0
	epsilon = 0
	for x in range(len(bits[0])):
		gamma <<= 1
		epsilon <<= 1
		if most_common_bit(bits, x) == 1:
			gamma |= 1
		else:
			epsilon |= 1
	return gamma * epsilon

def filter_by_bits(bits, match):
	for x in range(len(bits[0])):
		most_common = most_common_bit(bits, x)
		bits = list(filter(lambda line: (line[x] == most_common) == match, bits))
		if len(bits) == 1:
			break
	result = 0
	for bit in bits[0]:
		result <<= 1
		result |= bit
	return result

def find_life_support(bits):
	oxygen = filter_by_bits(bits, True)
	scrubber = filter_by_bits(bits, False)
	return oxygen * scrubber

print('Part 1:', find_power_consumption(bits))
print('Part 2:', find_life_support(bits))