def constructPriorityList():
    plist = {}
    priority = 1
    for i in range(ord("a"), ord("z") + 1):
        plist[chr(i)] = priority
        priority += 1
    priority = 27
    for i in range(ord("A"), ord("Z") + 1):
        plist[chr(i)] = priority
        priority += 1
    return plist

priorityList = constructPriorityList()

lines = []
for line in open("input.txt").readlines():
    lines.append(line[:-1])

running_total = 0
for i in range(0, len(lines), 3):
    bp1Set = {char for char in lines[i]}
    bp2Set = {char for char in lines[i+1]}
    bp3Set = {char for char in lines[i+2]}
    intersect = bp1Set & bp2Set & bp3Set
    running_total += priorityList[intersect.pop()]

print(running_total)

