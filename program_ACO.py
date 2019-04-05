from ACO_TA import *
import random
import operator
from math import *
from statistics import *


def solveTA(jmlh_ant, jmlh_iterasi, jmlh_agent, jmlh_caps, jmlh_task, w2, rho, alpha, beta, seed):
    random.seed(seed)

    a = jmlh_agent
    c = jmlh_caps
    n = jmlh_task
    w2 = w2
    agent_pos_x, agent_pos_y, agent_edges = createAgent.go(a,w2)

    """print(agent_pos_x)
    print(agent_pos_y)
    print(agent_edges)"""

    task_pos_x, task_pos_y, task_edges = createTask.go(n,a,w2,agent_pos_x,agent_pos_y)

    """print(task_pos_x)
    print(task_pos_y)
    print(task_edges)"""

    capability, cwf = generateCapability.go(a, c)
    #print(capability)
    #print(cwf)

    requiredCap = requiredCapability.go(n, c)
    #print(requiredCap)

    collection, task_needs = agentCollection.go(capability, requiredCap, a, c, n)
    #print(collection)

    """
        Algoritme ACO pada Task Allocation
    """
    # Inisialisasi parameter ACO

    antNo = jmlh_ant
    iterasi = jmlh_iterasi

    rho = rho
    alpha = alpha
    beta = beta

    phero_matrix = []
    for i in range(a):
        tau_0 = round(1 / (a * sum(agent_edges[i])), 5)
        phero_matrix.append([tau_0 for _ in range(a)])
        """for j in range(a):
            if i == j:
                phero_matrix[i].append(0)
            else:
                phero_matrix[i].append( tau_0 )"""

    #print(phero_matrix)
    # Main Loop of ACO

    bestEfficiency = 0
    bestTour = []
    efisiensi_iterasi = []
    cap_need = task_needs[0]  # Single Target
    #print(cap_need)

    for it in range(iterasi):
        colony_tour, colony_efficiency = createColony.go(antNo, collection, cwf, cap_need, alpha, beta, phero_matrix, agent_edges, task_edges)
        #print(olony_tour)
        #print(colony_efficiency)

        for i in range(antNo):
            efficiency = 0

        # Update global best
        max_index, max_value = max(enumerate(colony_efficiency), key=operator.itemgetter(1))
        if max_value > bestEfficiency:
            bestEfficiency = colony_efficiency[max_index]
            bestTour = colony_tour[max_index]

        # Update Pheromones
        phero_matrix = updatePheromone.go(phero_matrix, cap_need, colony_tour, colony_efficiency)

        # Evaporation
        for i in range(a):
            for j in range(a):
                phero_matrix[i][j] *= (1 - rho)
                phero_matrix[i][j] = round(phero_matrix[i][j],5)

        efisiensi_iterasi.append(bestEfficiency)

    #print(phero_matrix)
    #print(cwf)
    data = "Final Best Agent for the Task\t: " + str([x+1 for x in bestTour])
    return data
