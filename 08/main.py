def read_file(file):
    with open(file, "r") as f:
        data = [line.split(" | ")[1].split() for line in f]
    f.close()
    return data


def part_1(file):
    output_values = read_file(file)

    cpt = 0
    for value in output_values:
        for digit in value:
            if len(digit) in (2, 4, 3, 7):  # number of segments for 1, 4, 7, and 8
                cpt += 1

    return cpt


print("PART 1")
print(part_1("input-day08.txt"))

