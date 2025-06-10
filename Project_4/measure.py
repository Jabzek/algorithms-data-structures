import os
import csv
import time
from graph_create import create_graph


def time_execution(graph, hamiltonGraph):
    if hamiltonGraph:
        startTimeHamilton = time.time()
        graph.hamiltonian_cycle()
        endTimeHamilton = time.time()
        elapsedTimeHamilton = endTimeHamilton - startTimeHamilton

        startTimeEuler = time.time()
        graph.eulerian_cycle()
        endTimeEuler = time.time()
        elapsedTimeEuler = endTimeEuler - startTimeEuler
    else:
        startTimeHamilton = time.time()
        graph.hamiltonian_cycle()
        endTimeHamilton = time.time()
        elapsedTimeHamilton = endTimeHamilton - startTimeHamilton
        elapsedTimeEuler = None

    return elapsedTimeHamilton, elapsedTimeEuler


def measurements(numberofNodes, filename, hamiltonGraph): 
    for el in numberofNodes:
        graph = create_graph(hamiltonGraph, numberofNodes=el, measurements=True)
        elapsedTimeHamilton, elapsedTimeEuler = time_execution(graph, hamiltonGraph)

        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            if hamiltonGraph:
                writer.writerow(("Hamiltonian", el, elapsedTimeHamilton, elapsedTimeEuler))
            else:
                writer.writerow(("Non-Hamiltonian", el, elapsedTimeHamilton))


numberofNodes1 = [100, 200, 300, 400, 500, 600]
numberofNodes2 = [12, 13, 14, 15, 16, 17]

if __name__ == "__main__":
    programDir = os.path.dirname(__file__)
    filename = os.path.join(programDir, "measure.csv")
    
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(("Graph Type", "Number of Nodes", "Hamiltonian Cycle Time", "Eulerian Cycle Time"))
    
    for el in range(2):
        if el == 0:
            measurements(numberofNodes1, filename, hamiltonGraph=True)
        else:
            measurements(numberofNodes2, filename, hamiltonGraph=False)
