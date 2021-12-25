with open('day08.txt') as file:
    part1 = 0
    part2 = 0
    for line in file:
        line = line.strip()
        if (len(line) > 0):
            inputs, outputs = [[''.join(sorted(pattern)) for pattern in patterns.split()] for patterns in line.split(' | ')]

            digit_to_pattern = [None]*10

            for pattern in inputs:
                if len(pattern) == 2:
                    digit_to_pattern[1] = pattern
                elif len(pattern) == 4:
                    digit_to_pattern[4] = pattern
                elif len(pattern) == 3:
                    digit_to_pattern[7] = pattern
                elif len(pattern) == 7:
                    digit_to_pattern[8] = pattern

            def overlap(pattern, target):
                count = 0
                for segment in target:
                    if segment in pattern:
                        count += 1
                return count

            for pattern in inputs:

                #  Overlap table
                # --+-------------
                #   | 2 5 3 6 9 0
                # --+-------------
                # 1 | 1 1 2 1 2 2
                # 4 | 2 3 3 3 4 3  
                # 7 | 3 2 3 2 3 3
                # --+-------------

                if len(pattern) == 5: # Could be 2, 3, or 5
                    if overlap(pattern, digit_to_pattern[4]) == 2:
                        digit_to_pattern[2] = pattern
                    elif overlap(pattern, digit_to_pattern[1]) == 2:
                        digit_to_pattern[3] = pattern
                    else:
                        digit_to_pattern[5] = pattern
                elif len(pattern) == 6: # Could be 0, 6, or 9
                    if overlap(pattern, digit_to_pattern[1]) == 1:
                        digit_to_pattern[6] = pattern
                    elif overlap(pattern, digit_to_pattern[4]) == 4:
                        digit_to_pattern[9] = pattern
                    else:
                        digit_to_pattern[0] = pattern

            pattern_to_digit = { pattern:digit for digit, pattern in enumerate(digit_to_pattern) }

            number = 0
            for pattern in outputs:
                if len(pattern) == 2:
                    part1 += 1
                elif len(pattern) == 4:
                    part1 += 1
                elif len(pattern) == 3:
                    part1 += 1
                elif len(pattern) == 7:
                    part1 += 1
                number *= 10
                number += pattern_to_digit[pattern]

            part2 += number

    print('Part 1:', part1)
    print('Part 2:', part2)