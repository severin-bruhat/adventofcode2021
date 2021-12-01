def read_file(file):
    with open(file, "r") as f:
        depths = [int(l.strip()) for l in f.readlines()]
    f.close()
    return depths

# refactored version
def part_1(file):
    depths = read_file(file)

    cpt = 0;
    for i in range(len(depths)):
        if depths[i - 1] < depths[i]:
            cpt += 1

    print("Number of Increases: ", cpt)

# dirty initial version
# def part_1(file):
#     depths = read_file(file)
#
#     idx = 0
#     cpt = 0
#     previous_value = 0
#
#     for depth in depths:
#         if idx > 0:
#             if depth > previous_value:
#                 cpt += 1
#         previous_value = depth
#         idx = idx + 1
#
#     print("Number of Increases: ", cpt)

def part_2(file):
    depths = read_file(file)

    cpt = 0;
    for i in range(len(depths)):
        if sum(depths[i:i+3]) < sum(depths[i+1:i+4]):
            cpt += 1

    print("Number of Increases: ", cpt)


print("PART 1")
part_1("input-day01.txt")

print("PART 2")
part_2("input-day01.txt")