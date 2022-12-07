lines = []
for line in open("input.txt").readlines():
    lines.append(line.strip())

# All commands:
# cd - change directory
# cd x - in a level
# cd .. out a level
# cd / - master
# ls - list files/dir
#   123 abc - 123(size), abc(filename)
#   dir xyz - directory named xyz

from collections import defaultdict

dirSize = defaultdict(int) # Cool thing

currentPath = []

# We only need to account for cd .. or cd x. We don't need to know when they are using ls, we just need to know theyre not using cd, then we can just try and cast the 'filesize' to an integer, whether it is the filesize or dir.

for line in lines:
    line = line.split(" ")
    if line[1] == "cd":
        if line[2] == "..":
            currentPath.pop()
        else:
            currentPath.append(line[2])
    else:
        try:
            # convert to int, if it is not convertible then we except the error and continue (because it is a $ or "dir" name)
            filesize = int(line[0])
            # append to the current path filesize, and all the directories before.
            # for i in range(1, len(currentPath)+1): # +1 so inclusive, start at 1 because we dont want to incude the /
            #     path = "/".join(currentPath[0:i]) # path of all parents.
            for i in range(0, len(currentPath)+1): # +1 so inclusive of current dir.
                path = "".join(currentPath[:i]) # path of all parents.
                dirSize[path] += filesize
        except:
            continue


sumOfBelow100000 = 0 # part 1

for key, val in dirSize.items():
    if val <= 100000:
        sumOfBelow100000 += val

print(sumOfBelow100000) # Part 1