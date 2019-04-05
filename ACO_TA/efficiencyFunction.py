import random
from math import *


def go(tour, collection, cwf, requiredCap, agent_edges, task_edges):
    pembilang = []
    penyebut = []
    for i in range(len(requiredCap)):
        temp = cwf[collection[requiredCap[i]][0]][requiredCap[i]]
        pembilang.append(temp)

    for j in range(len(tour)-1):
        temp = agent_edges[tour[j]][tour[j+1]] + task_edges[0][tour[j]] + task_edges[0][tour[j+1]]
        penyebut.append(temp)

    efficiency = sum(pembilang) / sum(penyebut)
    efficiency = round(efficiency,5)

    return efficiency
