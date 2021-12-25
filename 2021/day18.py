class Node:
	def __init__(self, parent=None, *, num=None, left=None, right=None):
		self.parent = parent
		self.num = num
		self.left = left
		self.right = right

def copy(node: Node) -> Node:
	if node is None:
		return None
	result = Node()
	result.num = node.num
	result.left = copy(node.left)
	result.right = copy(node.right)
	if result.left is not None:
		result.left.parent = result
	if result.right is not None:
		result.right.parent = result
	return result

def magnitude(x: Node) -> int:
	if x.num is not None:
		return x.num
	else:
		return 3 * magnitude(x.left) + 2 * magnitude(x.right)

def find_root(node: Node) -> Node:
	while node.parent is not None:
		node = node.parent
	return node

def tree_to_list(node: Node) -> list[Node]:
	if node.num is not None:
		return [node]
	else:
		return tree_to_list(node.left) + tree_to_list(node.right)

def explode(x: Node, nesting=0) -> bool:
	if x.num is not None:
		return False
	elif nesting > 3:
		left = x.left.num
		right = x.right.num
		x.num = 0
		x.left = None
		x.right = None
		list = tree_to_list(find_root(x))
		index = list.index(x)
		if index > 0:
			list[index - 1].num += left
		if index < len(list) - 1:
			list[index + 1].num += right
		return True
	else:
		return explode(x.left, nesting + 1) or explode(x.right, nesting + 1)

def split(x: Node) -> bool:
	if x.num is None:
		if split(x.left):
			return True
		if split(x.right):
			return True
		return False
	else:
		if x.num >= 10:
			x.left = Node(x, num=(x.num+0)//2)
			x.right = Node(x, num=(x.num+1)//2)
			x.num = None
			return True
		else:
			return False

def reduce(x: Node):
	while True:
		did_explode = False
		while explode(x):
			did_explode = True
		did_split = split(x)
		if not (did_explode or did_split):
			break

def add(x: Node, y: Node) -> Node:
	sum = Node(None, left=x, right=y)
	x.parent = sum
	y.parent = sum
	reduce(sum)
	return sum

def parse_list(x: list, parent:Node=None) -> Node:
	if type(x) is int:
		return Node(parent, num=x)
	else:
		left, right = x
		result = Node(parent)
		result.left = parse_list(left, result)
		result.right = parse_list(right, result)
		return result

def parse(line: str) -> Node:
	import ast
	return parse_list(ast.literal_eval(line))


lines: list[Node] = []
with open('day18.txt') as file:
	for line in file:
		line = line.strip()
		if len(line) > 0:
			lines.append(parse(line))

def part1(lines: list[Node]):
	lines = lines.copy()
	for i in range(len(lines)):
		lines[i] = copy(lines[i])
	x = lines[0]
	for y in lines[1:]:
		x = add(x, y)
	return magnitude(x)

def part2(lines: list[Node]):
	n = len(lines)
	max_magnitude = 0
	for i in range(n):
		for j in range(n):
			x = copy(lines[i])
			y = copy(lines[j])
			sum = add(x, y)
			mag = magnitude(sum)
			if mag > max_magnitude:
				max_magnitude = mag
	return max_magnitude

print('Part 1:', part1(lines))
print('Part 2:', part2(lines))