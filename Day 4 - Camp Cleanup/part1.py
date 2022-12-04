lines = []
for line in open("input.txt").readlines():
    lines.append(line[:-1])

inclusive = 0
for line in lines:
    line = line.split(",")
    section1Start = int(line[0].split("-")[0])
    section1Stop = int(line[0].split("-")[1])
    section2Start = int(line[1].split("-")[0])
    section2Stop = int(line[1].split("-")[1])
    if (section1Start <= section2Start and section2Stop <= section1Stop) or (section2Start <= section1Start and section1Stop <= section2Stop):
        inclusive += 1

print(inclusive)