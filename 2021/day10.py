OPEN_TO_CLOSE = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>',
}

SYNTAX_SCORE = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137,
}

AUTOCOMPLETE_SCORE = {
    ')':1,
    ']':2,
    '}':3,
    '>':4,
}

syntax_score = 0
autocomplete_scores = []
with open('day10.txt') as file:
    for line in file:
        line = line.strip()
        if len(line) > 0:
            stack = []
            syntax_error = False
            for char in line:
                if char in OPEN_TO_CLOSE:
                    close = OPEN_TO_CLOSE[char]
                    stack.append(close)
                else:
                    if len(stack) > 0 and stack[-1] == char:
                        stack.pop()
                    else:
                        syntax_score += SYNTAX_SCORE[char]
                        syntax_error = True
                        break
            if not syntax_error:
                score = 0
                for char in reversed(stack):
                    score *= 5
                    score += AUTOCOMPLETE_SCORE[char]
                autocomplete_scores.append(score)

import statistics
autocomplete_score = statistics.median(autocomplete_scores)

print('Part 1:', syntax_score)
print('Part 2:', autocomplete_score)