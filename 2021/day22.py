with open('day22.txt') as file:
	lines = [line.strip() for line in file.readlines()]

def parse_commands(lines, min, max):
	commands = []
	for line in lines:
		command, coords_string = line.split()
		coords_separate_string = [coord[2:] for coord in coords_string.split(',')]
		cube = tuple((int(min), int(max) + 1) for min, max in [coord.split('..') for coord in coords_separate_string])
		outside = False
		for minv, maxv in cube:
			if minv < min or minv > max or maxv < min or maxv > max:
				outside = True
				break
		if outside: 
			continue
		commands.append((command, cube))
	return commands

def overlap(range1, range2):
	min1, max1 = range1
	min2, max2 = range2
	p1 = max(min1, min2)
	p2 = min(max1, max2)
	p2 = max(p1, p2)
	return (p1, p2)
		
def intersect(cube1, cube2):
	return (
		overlap(cube1[0], cube2[0]), 
		overlap(cube1[1], cube2[1]),
		overlap(cube1[2], cube2[2]))

def volume(cube):
	(min1, max1), (min2, max2), (min3, max3) = cube
	return (max1 - min1) * (max2 - min2) * (max3 - min3)

def activate(commands):
	on_cubes = []
	off_cubes = []
	on_volume = 0	
	for command, cube in commands:
		on, off = len(on_cubes), len(off_cubes)	
		if command == 'on':
			on_volume += volume(cube)
			on_cubes.append(cube)		
		for on_cube in on_cubes[:on]:
			i = intersect(cube, on_cube)
			v = volume(i)
			if v > 0:
				on_volume -= v
				off_cubes.append(i)			
		for off_cube in off_cubes[:off]:
			i = intersect(cube, off_cube)
			v = volume(i)
			if v > 0:
				on_volume += v
				on_cubes.append(i)
	return on_volume
				 	
print('Part 1:', activate(parse_commands(lines, -50, +50)))
print('Part 2:', activate(parse_commands(lines, -1e300, +1e300)))