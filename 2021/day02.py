x = 0
y = 0

with open('day02.txt') as file:
    for line in file:
        line = line.strip()
        cmd, arg = line.split()
        if cmd == 'forward':
            x += int(arg)
        elif cmd == 'down':
            y += int(arg)
        elif cmd == 'up':
            y -= int(arg)

print('Part 1:', x * y)

x = 0
y = 0
aim = 0

with open('day02.txt') as file:
    for line in file:
        line = line.strip()
        cmd, arg = line.split()
        if cmd == 'forward':
            x += int(arg)
            y += int(arg) * aim
        elif cmd == 'down':
            aim += int(arg)
        elif cmd == 'up':
            aim -= int(arg)

print('Part 2:', x * y)