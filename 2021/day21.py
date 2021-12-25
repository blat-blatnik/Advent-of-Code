with open('day21.txt') as file:
    line1 = file.readline().strip()
    line2 = file.readline().strip()
    p1_start = int(line1.split()[4])
    p2_start = int(line2.split()[4])

def mod_add(x, y, min, max):
    return min + ((x - min + y) % max)

def dict_add(d: dict, key, count):
    if key in d:
        d[key] += count
    else:
        d[key] = count

def part1():
    p1_pos = p1_start
    p2_pos = p2_start
    p1_score = 0
    p2_score = 0
    whose_turn = 0
    die = 1
    times_rolled = 0
    while True:
        roll = die
        die = mod_add(die, 1, 1, 100)
        roll += die
        die = mod_add(die, 1, 1, 100)
        roll += die
        die = mod_add(die, 1, 1, 100)
        times_rolled += 3
        if whose_turn == 0:
            p1_pos = mod_add(p1_pos, roll, 1, 10)
            p1_score += p1_pos
            if p1_score >= 1000:
                return p2_score * times_rolled
        else:
            p2_pos = mod_add(p2_pos, roll, 1, 10)
            p2_score += p2_pos
            if p2_score >= 1000:
                return p1_score * times_rolled
        whose_turn = int(not bool(whose_turn))

def part2():
    state = (p1_start, p2_start, 0, 0, 0) # p1_pos, p2_pos, p1_score, p2_score, whose_turn
    state_counts = { state:1 }
    p1_wins = 0
    p2_wins = 0
    while len(state_counts) > 0:
        next_state_counts = {}
        for state in state_counts:
            count = state_counts[state]
            for roll, possible_ways in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
                p1_pos, p2_pos, p1_score, p2_score, whose_turn = state
                if whose_turn == 0:
                    p1_pos = mod_add(p1_pos, roll, 1, 10)
                    p1_score += p1_pos
                    if p1_score >= 21:
                        p1_wins += possible_ways * count
                    else:
                        next_state = (p1_pos, p2_pos, p1_score, p2_score, 1)
                        dict_add(next_state_counts, next_state, possible_ways * count)
                else:
                    p2_pos = mod_add(p2_pos, roll, 1, 10)
                    p2_score += p2_pos
                    if p2_score >= 21:
                        p2_wins += possible_ways * count
                    else:
                        next_state = (p1_pos, p2_pos, p1_score, p2_score, 0)
                        dict_add(next_state_counts, next_state, possible_ways * count)
        state_counts = next_state_counts
    return max(p1_wins, p2_wins)

print('Part 1:', part1())
print('Part 2:', part2())