links = []
with open('day12.txt') as file:
    for line in file:
        line = line.strip()
        if len(line) > 0:
            a, b = line.split('-')
            links.append((a, b))
            links.append((b, a))
    
def count_paths(current, visited, small_visit):
    if current == 'end':
        return 1

    visited = visited.copy()
    if current.islower():
        visited.add(current)
    
    count = 0
    for a, b in links:
        if a == current and (b not in visited or (small_visit and b != 'start')):
            if b in visited and small_visit:
                count += count_paths(b, visited, False)
            else:
                count += count_paths(b, visited, small_visit)
    return count

print('Part 1:', count_paths('start', {'start'}, False))
print('Part 2:', count_paths('start', {'start'}, True))
