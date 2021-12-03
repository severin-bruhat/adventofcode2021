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


print("PART 1")
print(part_1("input-day03.txt")) #output: 738234