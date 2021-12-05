import numpy as np


def read_file(file):
    with open(file, "r") as f:
        data = [l.strip() for l in f.readlines()]
    f.close()
    return data


def get_range(value1, value2):
    if value1 < value2:
        return [x for x in range(value1, value2+1)]
    return [x for x in range(value1, value2-1, -1)]

# https://www.reddit.com/r/adventofcode/comments/r9824c/2021_day_5_solutions/


def part_1(file):
    coordinates = read_file(file)
    diagram = np.zeros([1000, 1000])

    for coord in coordinates:
        pair1, pair2 = coord.split("->")
        x1, y1 = pair1.split(",")
        x2, y2 = pair2.split(",")
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        if x1 == x2:  # moving horizontally
            range_y = get_range(y1, y2)
            for y in range_y:
                diagram[y][x1] += 1

        elif y1 == y2:  # moving vertically
            range_x = get_range(x1, x2)
            for x in range_x:
                diagram[y1][x] += 1

    print(np.count_nonzero(diagram > 1))


print("PART 1")
part_1("input-day05.txt")