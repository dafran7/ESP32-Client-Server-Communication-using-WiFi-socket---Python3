import random
from math import *


def go(n, a, w2, agent_pos_x, agent_pos_y):
    x = []
    y = []

    for i in range(n):
        x.append(random.randrange(0,100000*30)/100000)
        y.append(random.randrange(0,100000*30)/100000)

    task_pos_x = x
    task_pos_y = y

    task_edges = [[0] * a for _ in range(n)]

    for i in range(n):
        for j in range(a):
            task_edges[i][j] = w2 * sqrt((task_pos_x[i] - agent_pos_x[j])**2 + (task_pos_y[i] - agent_pos_y[j])**2)
            task_edges[i][j] = round(task_edges[i][j], 5)

    return task_pos_x, task_pos_y, task_edges
