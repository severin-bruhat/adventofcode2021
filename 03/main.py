def read_file(file):
    with open(file, "r") as f:
        data = [l.strip() for l in f.readlines()]
    f.close()
    return data


def part_1(file):
    gamma = epsilon = ''
    diagnostic = read_file(file)

    for index in range(len(diagnostic[0])):
        s0 = s1 = 0
        for number in diagnostic:
            if number[index] == '0':
                s0 += 1
            if number[index] == '1':
                s1 += 1

        if s0 > s1:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return int(gamma, 2) * int(epsilon, 2)

######################## PART 2 ########################


def filter(position, rows, bit):
    rows0 = []
    rows1 = []

    if len(rows) == 1 or position == 12:
        return rows[0]

    for row in rows:
        if row[position] == '0':
            rows0.append(row)
        elif row[position] == '1':
            rows1.append(row)

    if bit == '1':
        return filter(position + 1, rows1 if len(rows1) >= len(rows0) else rows0, bit)
    elif bit == '0':
        return filter(position + 1, rows0 if len(rows0) <= len(rows1) else rows1, bit)


def part_2(file):
    diagnostic = read_file(file)

    oxygen = filter(0, diagnostic, '1')
    co2 = filter(0, diagnostic, '0')
    life_support = int(oxygen, 2) * int(co2, 2)

    print("oxygen", oxygen)
    print("co2", co2)
    print("life_support", life_support)


print("PART 1")
print(part_1("input-day03.txt"))


print("PART 2")
print(part_2("input-day03.txt"))