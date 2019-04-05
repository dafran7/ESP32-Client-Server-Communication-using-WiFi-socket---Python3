import random
from math import *


def go(capability, reqd_caps, a, c, n):
    task_needs = [[] for _ in range(n)]

    for i in range(n):
        for j in range(c):
            if reqd_caps[i][j] == 1:
                task_needs[i].append(j)

    collection = []

    for i in range(c):
        team_up = []
        for j in range(a):
            if capability[j][i] == 1:
                team_up.append(j)    # +1 untuk index dari 1
        collection.append(team_up)

    return collection, task_needs
