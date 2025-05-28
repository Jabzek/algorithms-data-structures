import math
import os
import random

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
        circleRadius = 3  
        tikz = []

        tikz.append("\\documentclass{standalone}")
        tikz.append("\\usepackage{tikz}")
        tikz.append("\\begin{document}")
        tikz.append("\\begin{tikzpicture}[scale=1, every node/.style={circle, draw}]")

        # Calculate nodes coordinates
        positions = []
        for i in range(self.numberofNodes):
            angle = 2 * math.pi * i / self.numberofNodes
            x = circleRadius * math.cos(angle)
            y = circleRadius * math.sin(angle)
            positions.append((x, y))
            tikz.append(f"\\node (N{i+1}) at ({x:.2f},{y:.2f}) {{{i+1}}};")

        # Add edges
        for i in range(self.numberofNodes):
            for j in range(i+1, self.numberofNodes):
                if self.matrixRepresentation[i][j]:
                    tikz.append(f"\\draw (N{i+1}) -- (N{j+1});")

        tikz.append("\\end{tikzpicture}")
        tikz.append("\\end{document}")

        scriptDir = os.path.dirname(__file__) #Get the directory of the script
        outputDir = os.path.join(scriptDir, "graph_visualization")
        filename = os.path.join(outputDir, "graph_tikz.tex") 
        
        with open(filename, "w", encoding="utf-8") as file:
            for line in tikz:
                file.write(line + "\n")
        print("Eksportowano do graph_tikz.tex\n")
    
    
    def hamiltonian_cycle(self):
        
        def hamiltonian(currentNode, path, visitedNodes): 
            visitedNodes[currentNode] = True

            for i in range(self.numberofNodes):
                if self.matrixRepresentation[currentNode][i] == 1 and not visitedNodes[i]:
                    path.append(i + 1)
                    if len(path) == self.numberofNodes:  
                        if self.matrixRepresentation[path[-1] - 1][path[0] - 1] == 1:  #Check if the last node connects to the first
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
        # Check if all nodes have even degree
        for i in range(self.numberofNodes):
            degree = sum(self.matrixRepresentation[i])
            if degree % 2 != 0:
                print("Graf nie ma cyklu Eulera (nie wszystkie wierzchołki są stopnia parzystego).\n")
                return None

        while True:
            start = random.randint(0, self.numberofNodes - 1)
            if sum(self.matrixRepresentation[start]) > 0:
                break

        copyofGraph = [row[:] for row in self.matrixRepresentation]
        stack = [start]  
        path = []

        while stack:
            v = stack[-1]
            found = False
            for u in range(self.numberofNodes):
                if copyofGraph[v][u]:
                    copyofGraph[v][u] = 0
                    copyofGraph[u][v] = 0
                    stack.append(u)
                    found = True
                    break
            if not found:
                path.append(stack.pop())

        path = [v + 1 for v in path[::-1]]  
        print("Znaleziono cykl Eulera: " + " -> ".join(str(node) for node in path))
        print()
        return path    
    