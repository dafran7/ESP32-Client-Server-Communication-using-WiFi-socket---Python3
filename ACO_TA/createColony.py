import random
from math import *
from . import efficiencyFunction


def go(antNo, collection, cwf, requiredCap, alpha, beta, pheromone_matrix, agent_edges, task_edges):

    first_col = collection[0]
    ant_tour = []
    efficiency = []
    for i in range(antNo):
        initial_node = random.randint(0,len(first_col)-1)
        tour = [first_col[initial_node]]

        for k in range(1,len(requiredCap)):
            currentNode = tour[-1]
            temp = []
            #temp = [[] for _ in range(len(collection[requiredCap[k]]))]
            for t in range(len(collection[requiredCap[k]])):
                pembilang = cwf[currentNode][requiredCap[k-1]] + cwf[collection[requiredCap[k]][t]][requiredCap[k]]
                penyebut = agent_edges[currentNode][collection[requiredCap[k]][t]] + task_edges[0][currentNode] + task_edges[0][collection[requiredCap[k]][t]]
                nij = pembilang / penyebut
                hitung = pheromone_matrix[currentNode][collection[requiredCap[k]][t]]**alpha + nij**beta
                temp.append(hitung)
            probability = [round(z/sum(temp),5) for z in temp]
            rand_number = random.randrange(0,100000)/100000
            prob_cummulative = 0
            nextNode = -1
            for p in range(len(probability)):
                prob_cummulative += probability[p]
                if rand_number < prob_cummulative:
                    nextNode = collection[requiredCap[k]][p]
                    break

            tour.append(nextNode)
        ant_tour.append(tour)

        # Fungsi efisiensi
        efficiency.append( efficiencyFunction.go(tour, collection, cwf, requiredCap, agent_edges, task_edges) )

    return ant_tour, efficiency
