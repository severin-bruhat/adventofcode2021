from enum import Enum


class Command(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"


def read_file(file):
    with open(file, "r") as f:
        commands = [l.strip() for l in f.readlines()]
    f.close()
    return commands


# refactored version
def part_1(file):
    command_entries = read_file(file)
    horizontal_value = 0
    vertical_value = 0

    for entry in command_entries:
        direction, units = entry.split()
        if direction == Command.DOWN.value:
            vertical_value += int(units)
        elif direction == Command.UP.value:
            vertical_value -= int(units)
        elif direction == Command.FORWARD.value:
            horizontal_value += int(units)

    res = horizontal_value * vertical_value

    print(res)


print("PART 1")
part_1("input-day02.txt")

