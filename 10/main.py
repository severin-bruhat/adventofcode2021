def read_file(file):
    with open(file, "r") as f:
        data = [l.strip() for l in f.readlines()]
    f.close()
    return data


def part_1(file):
    navigation_input = read_file(file)
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    illegal_char_points = {')': 3, ']': 57, '}': 1197, '>': 25137}

    error_score = 0

    for line in navigation_input:
        chunks = []
        for ch in line:
            if ch in pairs:
                chunks.append(ch)
            else:
                if ch != pairs[chunks.pop()]:
                    error_score += illegal_char_points[ch]
                    chunks = []
                    break

    return error_score


print("PART 1")
print(part_1("input-day10.txt"))
