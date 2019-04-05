import random
from math import *


def go(pheromone_matrix, requiredCap, colony_tour, colony_efficiency):
    capNo = len(requiredCap)
    antNo = len(colony_tour)

    for i in range(antNo):
        for j in range(capNo-1):
            currentNode = colony_tour[i][j]
            nextNode = colony_tour[i][j+1]

            pheromone_matrix[currentNode][nextNode] += colony_efficiency[i]

    return pheromone_matrix
