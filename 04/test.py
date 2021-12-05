with open("input-day04.txt") as txt:
    file = txt.read().strip().split("\n\n")

parts = [0, 0]
calls = [int(n) for n in file[0].split(',')]
winningturns = 999
losingturns = -999

for c in file[1:-1]:
    cardrows = [[0 for j in range(5)] for i in range(5)]
    cardcols = [[0 for j in range(5)] for i in range(5)]
    turns = -1
    bingo = False
    cardtotal = 0

    for i, line in enumerate(c.split('\n')):
        for j, num in enumerate(line.split()):
            cardrows[i][j] = int(num)
            cardcols[j][i] = int(num)
            cardtotal += int(num)

    while not bingo:
        turns += 1
        for i in range(len(cardrows)):
            for j in range(len(cardrows[0])):
                if cardrows[i][j] == calls[turns]:
                    cardtotal -= calls[turns]
                    cardrows[i][j] = -1
                    cardcols[j][i] = -1

                    for line in cardrows + cardcols:
                        if line == [-1, -1, -1, -1, -1]:
                            bingo = True

    if turns < winningturns:
        winningturns = turns
        parts[0] = cardtotal * calls[turns]

    if turns > losingturns:
        losingturns = turns
        parts[1] = cardtotal * calls[turns]

print(parts)

[42656, 10052, 8404, 23684, 44745, 26605, 15334, 15600, 14265, 29260, 44204, 40854, 25536, 12038, 4809, 38874, 36549, 9000, 20531, 14355, 14355, 14240, 647, 34658, 9728, 9728, 37290, 57570, 38280, 25748, 17152, 33573, 9600, 9600, 16892, 13995, 13995, 28576, 72814, 38106, 12789, 54275, 31110, 9308, 27846, 8064, 22386, 16704, 12852, 9080, 49126, 23790, 28730, 40629, 28545, 24570, 33215, 243, 243, 15795, 19902, 6248, 31992, 28126, 34965, 19647, 15660, 7600, 7304, 7304, 46909, 508, 21824, 7656, 7656, 50915, 33387, 61146, 39804, 16128, 18879, 33759, 15876, 15876, 12480, 41053, 12766, 59565, 13158, 14314, 26158, 14632, 15360, 31416, 4655, 4655, 26838, 36960, 45999, 23622, 28086, 6160, 34286, 37152, 9196, 17760, 24366, 51888, 31844]
