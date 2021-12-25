with open('day01.txt') as file:
    input = [int(line) for line in file.readlines()]

def count_increasing(array):
    count = 0
    for i in range(len(array) - 1):
        if array[i + 1] > array[i]:
            count +=1
    return count

def sliding_window(array):
    window = [0]*(len(array)-2)
    for i in range(len(array)-2):
        window[i] = array[i] + array[i + 1] + array[i + 2]
    return window

print('Part 1:', count_increasing(input))
print('Part 2:', count_increasing(sliding_window(input)))
