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


    def export_to_tickz(self):
        pass
    
    
    def hamiltonian_cycle(self):
        
        def hamiltonian(currentNode, path, visitedNodes): 
            visitedNodes[currentNode] = True

            for i in range(self.numberofNodes):
                if self.matrixRepresentation[currentNode][i] == 1 and not visitedNodes[i]:
                    path.append(i + 1)
                    if len(path) == self.numberofNodes:
                        if self.matrixRepresentation[path[-1] - 1][path[0] - 1] == 1:
                            return True       
                    if hamiltonian(i, path, visitedNodes):
                        return True
                    
            visitedNodes[currentNode] = False
            path.pop()          
            return False   
        
        for i in range(self.numberofNodes):
            path = [i + 1]
            visitedNodes = [False] * self.numberofNodes
            if hamiltonian(i, path, visitedNodes):
                print("Znaleziono cykl Hamiltona: " + " -> ".join(str(node) for node in path + [path[0]]))
                print()
                return
        print("Nie znaleziono cyklu Hamiltona w grafie.\n")
        

        

    def eulerian_cycle(self):
        pass    
    