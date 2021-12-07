import numpy as np


def read_file(file):
    with open(file, "r") as f:
        data = f.read()
        data_int = [int(x) for x in data.split(",")]
    f.close()
    return data_int


def part_1(file):
    crabs = read_file(file)

    max_pos = max(crabs)
    min_pos = min(crabs)
    crab_fuel = []

    for x in range(min_pos, max_pos - 1):
        fuel = 0

        for crab in crabs:
            fuel += abs(crab - x)
        crab_fuel.append((x, fuel))

    crab_fuel.sort(key=lambda p: p[1])

    return crab_fuel[0][1]


def part_1_optim(file):
    crabs = read_file(file)

    median = np.median(crabs)
    fuel = np.sum(np.abs(crabs - median))

    return int(fuel)


print("PART 1")
print("cost", part_1("input-day07.txt"))  # output 343605.0

print("PART 1 optim")
print("cost", part_1_optim("input-day07.txt"))  # output 343605.0


