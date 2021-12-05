def read_file(file):
    with open(file, "r") as f:
        data = f.read().strip().split("\n\n")
    f.close()
    return data


def bingo(winner):
    bingo_data = read_file("input-day04.txt")
    random_numbers = [int(n) for n in bingo_data[0].split(',')]
    bingo_cards = bingo_data[1:]
    win_idx = len(random_numbers)
    lose_idx = -len(random_numbers)
    score = 0

    for card in bingo_cards:
        rows = [[0 for j in range(5)] for i in range(5)]
        cols = [[0 for j in range(5)] for i in range(5)]
        card_total = 0
        draw_idx = -1
        finished = False

        # prepare the bingo cards, arrays for columns and rows
        for i, line in enumerate(card.split('\n')):
            for j, num in enumerate(line.split()):
                rows[i][j] = int(num)
                cols[j][i] = int(num)
                card_total += int(num)

        # drawing
        while not finished:
            draw_idx += 1
            for i in range(len(rows)):
                for j in range(len(rows[0])):
                    if rows[i][j] == random_numbers[draw_idx]:
                        # remove draw values (as we don't need them for the calculation)
                        rows[i][j] = '*'
                        cols[j][i] = '*'
                        # re-calculate the score of the card
                        card_total -= random_numbers[draw_idx]

                        # look for a completed row or column
                        for line in rows + cols:
                            if line == ["*", "*", "*", "*", "*"]:
                                finished = True

        if winner == "me" and draw_idx < win_idx:
            win_idx = draw_idx
            score = card_total * random_numbers[draw_idx]

        if winner == "squid" and draw_idx > lose_idx:
            lose_idx = draw_idx
            score = card_total * random_numbers[draw_idx]

    print(score)


def part_1():
    bingo("me")


def part_2():
    bingo("squid")

print("PART 1")
part_1() #expected output 54275


print("PART 2")
part_2() #expected output 13158