chars = open("input.txt").readlines()[0][:-1]

last4chars = []
charcount = 0
for char in chars:
    last4chars.append(char)
    charcount += 1
    if len(last4chars) == 4:
        if len(set(last4chars)) == 4:
            print("unique")
            print(charcount)
        else:
            last4chars.pop(0)

# Something fishy here but it works