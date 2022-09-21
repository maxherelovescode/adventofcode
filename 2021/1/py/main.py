import os
print("Started")
with open("input.txt", 'r') as f:
    inputfile = f.readline()
    for i in inputfile:
        dmi = 0
        previous = i
        if previous == 0:
            continue
        if previous == 9299:
            break
        else:
            if i > previous:
                dmi = dmi + 1
            else:
                continue
    print(dmi)
