def read_file(file):
    with open(file, "r") as f:
        data = [l.strip() for l in f.readlines()]
    f.close()
    return data


def part_1(file):
    input = read_file(file)
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    result = 0
    incomplete = []

    for line in input:
        chunks = []
        for char in line:
            if char in pairs:
                chunks.append(char)
            else:
                if char != pairs[chunks.pop()]:
                    result += scores[char]
                    chunks = []
                    break
        if chunks:
            incomplete.append(chunks)  # for part 2
    return result, incomplete


def part_2(incomplete):
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    result = []
    for line in incomplete:
        points = 0
        for ch in reversed(line):
            points = points * 5 + scores[ch]
        result.append(points)
    final = sorted(result)
    return final[len(final) // 2]


print("PART 1")
incomplete = part_1("input-day10.txt")[1]
print(part_1("input-day10.txt")[0])


print("PART 2")
print(part_2(incomplete))
