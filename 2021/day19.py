from math import dist


ORIENTATIONS = [
	((+1, 0, 0), ( 0,+1, 0), ( 0, 0,+1)),
	((+1, 0, 0), ( 0,-1, 0), ( 0, 0,-1)),
	((+1, 0, 0), ( 0, 0,+1), ( 0,-1, 0)),
	((+1, 0, 0), ( 0, 0,-1), ( 0,+1, 0)),
	((-1, 0, 0), ( 0,+1, 0), ( 0, 0,-1)),
	((-1, 0, 0), ( 0,-1, 0), ( 0, 0,+1)),
	((-1, 0, 0), ( 0, 0,+1), ( 0,+1, 0)),
	((-1, 0, 0), ( 0, 0,-1), ( 0,-1, 0)),
	(( 0,+1, 0), (+1, 0, 0), ( 0, 0,-1)),
	(( 0,+1, 0), (-1, 0, 0), ( 0, 0,+1)),
	(( 0,+1, 0), ( 0, 0,+1), (+1, 0, 0)),
	(( 0,+1, 0), ( 0, 0,-1), (-1, 0, 0)),
	(( 0,-1, 0), (+1, 0, 0), ( 0, 0,+1)),
	(( 0,-1, 0), (-1, 0, 0), ( 0, 0,-1)),
	(( 0,-1, 0), ( 0, 0,+1), (-1, 0, 0)),
	(( 0,-1, 0), ( 0, 0,-1), (+1, 0, 0)),
	(( 0, 0,+1), (+1, 0, 0), ( 0,+1, 0)),
	(( 0, 0,+1), (-1, 0, 0), ( 0,-1, 0)),
	(( 0, 0,+1), ( 0,+1, 0), (-1, 0, 0)),
	(( 0, 0,+1), ( 0,-1, 0), (+1, 0, 0)),
	(( 0, 0,-1), (+1, 0, 0), ( 0,-1, 0)),
	(( 0, 0,-1), (-1, 0, 0), ( 0,+1, 0)),
	(( 0, 0,-1), ( 0,+1, 0), (+1, 0, 0)),
	(( 0, 0,-1), ( 0,-1, 0), (-1, 0, 0)),
]

def num_matches(scanner1, scanner2):
	return len(set(scanner1) & set(scanner2))

def orient(points, ox, oy, oz):
	result = []
	for x, y, z, in points:
		rx = x*ox[0] + y*oy[0] + z*oz[0]
		ry = x*ox[1] + y*oy[1] + z*oz[1]
		rz = x*ox[2] + y*oy[2] + z*oz[2]
		result.append((rx, ry, rz))
	return result

def transform(points, ox, oy, oz, tx, ty, tz):
	result = []
	for x, y, z, in points:
		rx = x*ox[0] + y*oy[0] + z*oz[0]
		ry = x*ox[1] + y*oy[1] + z*oz[1]
		rz = x*ox[2] + y*oy[2] + z*oz[2]
		result.append((rx + tx, ry + ty, rz + tz))
	return result

def try_match(scanner1, scanner2):
	for ox, oy, oz in ORIENTATIONS:
		oriented2 = orient(scanner2, ox, oy, oz)
		for x1, y1, z1 in scanner1:
			for x2, y2, z2 in oriented2:
				tx = x1 - x2
				ty = y1 - y2
				tz = z1 - z2
				translated = [(x + tx, y + ty, z + tz) for x, y, z in oriented2]
				count = num_matches(scanner1, translated)
				if count >= 12:
					return translated, tx, ty, tz
	return None, None, None, None

def align(scanners: list, index: int, all_points: set, processed: set, offsets: list):
	processed.add(index)
	scanner1 = scanners[index]
	all_points |= set(scanner1)
	for i in range(len(scanners)):
		if i not in processed:
			scanner2 = scanners[i]
			aligned, tx, ty, tz = try_match(scanner1, scanner2)
			if aligned is not None:
				scanners[i] = aligned
				offsets[i] = (tx, ty, tz)
				align(scanners, i, all_points, processed, offsets)

scanners = []
with open('day19.txt') as file:
	scanner = None
	for line in file:
		line = line.strip()
		if len(line) > 0:
			if line.startswith('---'):
				if scanner is not None:
					scanners.append(scanner)
				scanner = []
			else:
				x, y, z = [int(val) for val in line.split(',')]
				scanner.append((x, y, z))
	scanners.append(scanner)

all_points = set()
processed = set()
offsets = [(0, 0, 0) for _ in scanners]
align(scanners, 0, all_points, processed, offsets)

max_distance = 0
n = len(scanners)
for i in range(n):
	for j in range(n):
		x1, y1, z1 = offsets[i]
		x2, y2, z2 = offsets[j]
		distance = abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)
		max_distance = max(max_distance, distance)

print('Part 1:', len(all_points))
print('Part 2:', max_distance)

