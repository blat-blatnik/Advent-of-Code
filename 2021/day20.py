with open('day20.txt') as file:
    lines = [line.strip() for line in file.readlines()]
    enhancement = lines[0]
    image = lines[2:]

def count(image, target):
    count = 0
    for row in image:
        for pixel in row:
            if pixel == target:
                count += 1
    return count

def enhance(image, enhancement, times):
    pad = '.'
    for _ in range(times):
        old_h = len(image)
        old_w = len(image[0])
        new_h = old_h + 2
        new_w = old_w + 2
        new_image = [[pad for _ in range(new_w)] for _ in range(new_h)]
        for y in range(-1, old_h + 1):
            for x in range(-1, old_w + 1):
                index = 0
                for ny in range(y - 1, y + 2):
                    for nx in range(x - 1, x + 2):
                        if ny >= 0 and ny < old_h and nx >= 0 and nx < old_w:
                            pixel = image[ny][nx]
                        else:
                            pixel = pad
                        index <<= 1
                        if pixel == '#':
                            index |= 1
                new_image[1 + y][1 + x] = enhancement[index]
        pad_index = 0b111111111 if pad == '#' else 0
        pad = enhancement[pad_index]
        image = new_image
    return image

print('Part 1:', count(enhance(image, enhancement, 2), '#'))
print('Part 2:', count(enhance(image, enhancement, 50), '#'))