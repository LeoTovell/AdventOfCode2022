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

running_total = 0

for line in open("input.txt").readlines():
    backpack = line[:-1]

    midpoint = len(backpack) //2

    firstCompartmentSet = {char for char in backpack[:midpoint]}
    secondCompartmentSet = {char for char in backpack[midpoint:]}

    duplicateItem = firstCompartmentSet & secondCompartmentSet

    running_total += priorityList[duplicateItem.pop()]

# print(running_total)

# One liner (two liner): 
priorityList = constructPriorityList()
print(sum([priorityList[({char for char in line[:-1][:len(line[:-1])//2]} & {char for char in line[:-1][len(line[:-1]) //2:]}).pop()] for line in open("input.txt").readlines()]))