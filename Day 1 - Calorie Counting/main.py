filename = "input.txt"

lines = open(filename).readlines()

# Part 1

c = []
rt = 0
for line in lines:
    if line == "\n":
        c.append(rt)
        rt = 0
    else:
        rt += int(line[:-1])
print(c.sort())
part1 = c[len(c) -1]
print(f"Part 1: {part1}")

# One line it?

p = "1" if True else "2"
print(p)

# Part 2
total = 0
for i in range(1,4):
    total += c[len(c) - i]

print(f"Part 2: {total}")