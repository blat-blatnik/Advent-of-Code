with open('day06.txt') as file:
    pop = [int(x) for x in file.readline().split(',')]

bins = [0] * 9
for p in pop:
    bins[p] += 1

def simulate(bins, days):
    for day in range(days):
        new_bins = [0] * len(bins)
        for i in range(8):
            new_bins[i] += bins[i + 1]
        new_bins[8] += bins[0]
        new_bins[6] += bins[0]
        bins = new_bins
    return sum(bins)

print('Part 1:', simulate(bins, 80))
print('Part 2:', simulate(bins, 256))