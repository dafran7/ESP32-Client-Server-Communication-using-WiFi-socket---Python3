import random
from math import *


def go(a, c):
    capability = [[0] * c for _ in range(a)]

    for i in range(a):
        cap_must = random.randint(1,10)
        cap_count = 0
        for j in range(c):
            if cap_count == cap_must:
                break
            have = random.randint(0,1)
            capability[i][j] = have
            if have == 1:
                cap_count += 1

    W1 = []
    for i in range(c):
        weight = 0.1 + random.randrange(0, 100000 * (0.8 - 0.1)) / 100000
        W1.append(weight)

    cwf = [[0] * c for _ in range(a)]
    for i in range(a):
        for j in range(c):
            cwf[i][j] = W1[j] * capability[i][j]
            cwf[i][j] = round(cwf[i][j],5)

    return capability, cwf
