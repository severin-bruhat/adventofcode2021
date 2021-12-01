def read_file(file):
    with open(file, "r") as f:
        depths = [int(l.strip()) for l in f.readlines()]
    f.close()
    return depths

def part_1(file):
    depths = read_file(file)

    idx = 0
    cpt = 0
    previous_value = 0

    for depth in depths:
        if idx > 0:
            if depth > previous_value:
                cpt += 1
        previous_value = depth
        idx = idx + 1

    print("Number of Increases: ", cpt)


print("PART 1")
part_1("input-day01.txt")