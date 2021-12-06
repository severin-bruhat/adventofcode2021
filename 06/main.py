def read_file(file):
    with open(file, "r") as f:
        data = f.read().strip().split(",")
    f.close()
    return data


def part_1(file):
    lanternfishs = read_file(file)

    for i in range(80):
        idx = 0
        for fish in lanternfishs:
            if int(fish) == 0:
                lanternfishs[idx] = 6
                lanternfishs.append(9)
            else:
                lanternfishs[idx] = int(lanternfishs[idx]) - 1

            idx += 1

    return len(lanternfishs)


print(part_1("input-day06.txt"))
