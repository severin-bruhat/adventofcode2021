def read_file(file):
    with open(file, "r") as f:
        data = [list(map(int, l.strip())) for l in f.readlines()]
    f.close()
    return data

def index_in_list(values, index):  # check the borders
    return index < len(values)

def part_1(file):
    input = read_file(file)

    low_points = []
    row_idx = 0
    for row in input:
        for i in range(len(row)):
            # deal with non border cases
            if (index_in_list(row, i + 1) and row[i] < row[i + 1]  # right
                    and index_in_list(row, i - 1) and row[i] < row[i - 1]  # left
                    and index_in_list(input, row_idx - 1) and row[i] < input[row_idx - 1][i]  # up
                    and index_in_list(input, row_idx + 1) and row[i] < input[row_idx + 1][i]):  # down
                low_points.append(row[i] + 1)

            elif not index_in_list(row, i + 1):  # right border
                if row_idx - 1 < 0:  # top right corner
                    if row[i] < row[i - 1] and row[i] < input[row_idx + 1][i]:
                        low_points.append(row[i] + 1)
                elif row_idx + 1 > len(input) - 1:  # bottom right corner
                    if row[i] < row[i - 1] and row[i] < input[row_idx - 1][i]:
                        low_points.append(row[i] + 1)
                else:
                    if row[i] < row[i - 1] and row[i] < input[row_idx - 1][i] and row[i] < input[row_idx + 1][i]:
                        low_points.append(row[i] + 1)

            elif i - 1 < 0:  # left border
                if row_idx - 1 < 0:  # top left corner
                    if row[i] < row[i + 1] and row[i] < input[row_idx + 1][i]:
                        low_points.append(row[i] + 1)

                elif row_idx + 1 > len(input) - 1:  # bottom left corner
                    if row[i] < row[i + 1] and row[i] < input[row_idx - 1][i]:
                        low_points.append(row[i] + 1)
                else:
                    if row[i] < row[i + 1] and row[i] < input[row_idx - 1][i] and row[i] < input[row_idx + 1][i]:
                        low_points.append(row[i] + 1)

            elif row_idx + 1 > len(input) - 1:  # bottom
                if row[i] < row[i - 1] and row[i] < row[i + 1] and row[i] < input[row_idx - 1][i]:
                    low_points.append(row[i] + 1)

            elif row_idx - 1 < 0:  # top
                if row[i] < row[i - 1] and row[i] < row[i + 1] and row[i] < input[row_idx + 1][i]:
                    low_points.append(row[i] + 1)
        row_idx += 1

    return sum(low_points)


print("PART 1")
print(part_1("input-day09.txt"))
