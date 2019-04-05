import random
from math import *


def go(a, w2):
    x = []
    y = []

    for i in range(a):
        x.append(random.randrange(0,100000*30)/100000)
        y.append(random.randrange(0,100000*30)/100000)

    agent_pos_x = x
    agent_pos_y = y

    agent_edges = [[0] * a for _ in range(a)]

    for i in range(a):
        for j in range(a):
            if i == j:
                agent_edges[i][j] = 0
            else:
                agent_edges[i][j] = w2 * sqrt( (x[i] - x[j])**2 + (y[i] - y[j])**2 )
                agent_edges[i][j] = round(agent_edges[i][j],5)

    return agent_pos_x, agent_pos_y, agent_edges

