class Stack:
    def __init__(self, list):
        self.list = list

    def pop(self):
        return self.list.pop() if not self.isEmpty() else "List empty"

    def isEmpty(self):
        return len(self.list) == 0

    def add(self, item):
        self.list.append(item)
    
    def __str__(self):
        return str([i for i in self.list])

stacksInput = [["N", "R", "G", "P"], ["J","T","B","L","F","G","D","C"],["M","S","V"],["L","S","R","C","Z","P"],["P","S","L","V","C","W","D","Q"],["C","T","N","W","D","M","S"],["H","D","G","W","P"],["Z","L","P","H","S","C","M","V"],["R","P","F","L","W","G","Z"]]
stacks = []
for stack in stacksInput:
    stacks.append(Stack(stack))

lines = []
for line in open("input.txt").readlines()[10:]:
    line = line[:-1]
    line = line.split(" ")
    amount = int(line[1])
    fromStack = int(line[3])
    toStack = int(line[5])
    for i in range(amount):
        item = stacks[fromStack-1].pop()
        stacks[toStack-1].add(item)

part1 = ""
for stack in stacks:
    part1 += str(stack.pop())

print(part1)
