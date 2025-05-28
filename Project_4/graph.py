class Graph:
    def __init__(self, numberofNodes):
        self.matrixRepresentation = [[0] * numberofNodes for _ in range(numberofNodes)]

    def add_edges(self, a, b):
        self.matrixRepresentation[a - 1][b - 1] = 1
        self.matrixRepresentation[b - 1][a - 1] = 1

