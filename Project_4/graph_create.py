from graph import Graph
import random

def data_provide(hamiltonGraph):
    while True:
        try:
            numberofNodes = int(input("Podaj liczbę wierzchołków: "))
            if hamiltonGraph:
                saturation = int(input("Podaj stopień nasycenia grafu (30/70): "))
                if numberofNodes <= 0 or saturation != 30 and saturation != 70:
                    raise ValueError
            if not hamiltonGraph:
                saturation = 50
                if numberofNodes <= 0:
                    raise ValueError
            break
        except ValueError:
            print("Niepoprawne dane. Wpisz dane jeszcze raz.\n")
    return numberofNodes, saturation 


def draw_nodes(numberofNodes):
    nodesList = []
    for _ in range(numberofNodes):
        node = random.randint(1, numberofNodes)
        while node in nodesList:
            node = random.randint(1, numberofNodes)
        nodesList.append(node)
    return nodesList
    

def create_graph(hamiltonGraph, numberofNodes, measurements): 
    if not measurements: 
        if hamiltonGraph:
            numberofNodes, saturation = data_provide(hamiltonGraph=True)
        else:
            numberofNodes, saturation = data_provide(hamiltonGraph=False)
    else:
        if hamiltonGraph:
            saturation = 30
        else:
            saturation = 50

    graph = Graph(numberofNodes)
    
    maxNumberOfEdges = numberofNodes * (numberofNodes - 1) // 2
    numberofEdges = maxNumberOfEdges * saturation // 100
    nodesList = draw_nodes(numberofNodes)   # list of nodes in the graph which will create unique hamiltonian cycle
    countEdges = 0
    
    # create hamiltonian cycle
    for i in range(len(nodesList)):       
        a = nodesList[i % numberofNodes]
        b = nodesList[(i + 1) % numberofNodes]
        graph.add_edges(a, b)
        countEdges += 1

    # add random edges to the graph
    while countEdges < numberofEdges:       
        a = random.randint(1, numberofNodes)
        b = random.randint(1, numberofNodes)
        if a != b and graph.matrixRepresentation[a - 1][b - 1] == 0:
            graph.add_edges(a, b)
            countEdges += 1

    if not hamiltonGraph:
        node = random.randint(1, numberofNodes)
        for i in range(numberofNodes):
            if graph.matrixRepresentation[node - 1][i] == 1:
                graph.matrixRepresentation[node - 1][i] = 0
                graph.matrixRepresentation[i][node - 1] = 0

    return graph

