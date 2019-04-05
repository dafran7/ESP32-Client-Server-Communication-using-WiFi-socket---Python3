import random
from math import *


def go(n, c):
    reqd_caps = [[0] * c for _ in range(n)]

    for i in range(n):
        cap_must = random.randint(1, 10)
        cap_count = 0
        for j in range(c):
            if cap_count == cap_must:
                break
            have = random.randint(0, 1)
            reqd_caps[i][j] = have
            if have == 1:
                cap_count += 1

    return reqd_caps
