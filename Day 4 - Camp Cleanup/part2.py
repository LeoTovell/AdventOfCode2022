lines = []
for line in open("input.txt").readlines():
    lines.append(line[:-1])

def createSetFromRange(start, stop):
    return {i for i in range(start, stop+1)}

overlaps = 0
for line in lines:
    line = line.split(",")
    section1Start = int(line[0].split("-")[0])
    section1Stop = int(line[0].split("-")[1])
    section2Start = int(line[1].split("-")[0])
    section2Stop = int(line[1].split("-")[1])
    overlap = createSetFromRange(section1Start, section1Stop) & createSetFromRange(section2Start, section2Stop)
    overlaps += 1 if overlap else 0
print(overlaps)