filename = "input.txt"

scoreguide = {"X": 1, "Y": 2, "Z": 3, "L": 0, "D": 3, "W": 6}

# Rock > Paper < Scissors

# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors

def winorlose(opponent, player):
    if (opponent == "A" and player == "X") or (opponent == "B" and player == "Y") or (opponent == "C" and player == "Z"):
        return "D"
    if (opponent == "A" and player == "Z") or (opponent == "B" and player == "X") or (opponent == "C" and player == "Y"):
        return "L"
    if (opponent == "A" and player == "Y") or (opponent == "B" and player == "Z") or (opponent == "C" and player == "X"):
        return "W"

def addscore(outcome, play):
    return scoreguide[outcome] + scoreguide[play]


totalScore = 0

for line in open(filename).readlines():
    line = line[:-1].split(" ")
    totalScore += addscore(winorlose(line[0], line[1]), line[1])

print(totalScore)
