filename = "input.txt"

scoreguide = {"X": 1, "Y": 2, "Z": 3, "L": 0, "D": 3, "W": 6}

translator = {"X": "L", "Y": "D", "Z": "W"}

# Rock > Paper < Scissors

# A = Rock
# B = Paper
# C = Scissors

# X = Rock = 3
# Y = Paper = 2
# Z = Scissors = 1

# Scissors C:
# L = Rock
# D = Scissors
# W = Paper

# Paper B:
# L = Scissors
# D = Paper
# W = Rock

# Rock A:
# L = Paper
# D = Rock
# W = Scissors



def addscore(play, outcome):
    return scoreguide[play] + scoreguide[translator[outcome]]

def whatplay(opponent, outcome):
    outcome = translator[outcome]

    if (opponent == "A" and outcome == "D") or (opponent == "B" and outcome == "L") or (opponent == "C" and outcome == "W"):
        return "X" # Rock
    if (opponent == "A" and outcome == "W") or (opponent == "B" and outcome == "D") or (opponent == "C" and outcome == "L"):
        return "Y" # Paper
    if (opponent == "A" and outcome == "L") or (opponent == "B" and outcome == "W") or (opponent == "C" and outcome == "D"):
        return "Z" # Scissors

totalScore = 0

for line in open(filename).readlines():
    line = line[:-1].split(" ")
    totalScore += addscore(whatplay(line[0], line[1]), line[1])

print(totalScore)