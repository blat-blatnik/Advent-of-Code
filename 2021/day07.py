with open('day07.txt') as file:
    positions = [int(x) for x in file.readline().split(',')]

import statistics
median = int(statistics.median(positions))
average = int(statistics.mean(positions))

print('Part 1:', sum(abs(p - median) for p in positions))
print('Part 2:', sum(sum(x for x in range(1 + abs(p - average))) for p in positions))