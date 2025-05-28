class Graph:
    def __init__(self, numberofNodes):
        self.matrixRepresentation = [[0] * numberofNodes for _ in range(numberofNodes)]
        self.numberofNodes = numberofNodes

    def add_edges(self, a, b):
        self.matrixRepresentation[a - 1][b - 1] = 1
        self.matrixRepresentation[b - 1][a - 1] = 1

    def show_graph(self):
        rowsList = []
        rowsList.append("  | " + " ".join([str(i) for i in range(1, self.numberofNodes+1)]))
        rowsList.append("--+" + "-" * (self.numberofNodes * 2))

        for el in range(1, self.numberofNodes+1):
            rowsList.append(f"{el} | " + " ".join([str(self.matrixRepresentation[el-1][i]) for i in range(self.numberofNodes)]))       
        
        for row in rowsList:
            print(row)
        print()