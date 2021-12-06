from collections import Counter
import time
start_time = time.time()

def read_file(file):
    with open(file, "r") as f:
        data = f.read()
        data_int = [int(x) for x in data.split(",")]
    f.close()
    return data_int


def part_1(file):
    lanternfishs = read_file(file)

    for i in range(80):
        idx = 0
        for fish in lanternfishs:
            if fish == 0:
                lanternfishs[idx] = 6
                lanternfishs.append(9)
            else:
                lanternfishs[idx] = lanternfishs[idx] - 1

            idx += 1

    return len(lanternfishs)

def part_2(file):
    lanternfishs = Counter(read_file(file)) #Counter({1: 207, 2: 26, 4: 24, 5: 22, 3: 21})

    for i in range(256):
        count = lanternfishs[0]
        for i in range(8):
            lanternfishs[i] = lanternfishs[i + 1]
        lanternfishs[8] = count
        lanternfishs[6] += count

    return sum(lanternfishs.values())


print("PART 1")
print(part_1("input-day06.txt"))


print("PART 2")
print(part_2("input-day06.txt"))
print("--- %s seconds ---" % (time.time() - start_time))
