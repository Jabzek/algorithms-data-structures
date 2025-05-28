import math

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

        n = self.numberofNodes
        radius = 3  # promień okręgu
        tikz = []

        # Preambuła LaTeX
        tikz.append("\\documentclass{standalone}")
        tikz.append("\\usepackage{tikz}")
        tikz.append("\\begin{document}")
        tikz.append("\\begin{tikzpicture}[scale=1, every node/.style={circle, draw}]")

        # Oblicz współrzędne wierzchołków na okręgu
        positions = []
        for i in range(n):
            angle = 2 * math.pi * i / n
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            positions.append((x, y))
            tikz.append(f"\\node (N{i+1}) at ({x:.2f},{y:.2f}) {{{i+1}}};")

        # Dodaj krawędzie
        for i in range(n):
            for j in range(i+1, n):
                if self.matrixRepresentation[i][j]:
                    tikz.append(f"\\draw (N{i+1}) -- (N{j+1});")

        tikz.append("\\end{tikzpicture}")
        tikz.append("\\end{document}")

        # Zapisz do pliku
        with open("graph_tikz.tex", "w", encoding="utf-8") as f:
            for line in tikz:
                f.write(line + "\n")
        print("Eksportowano do graph_tikz.tex")
    
    
    def hamiltonian_cycle(self):
        visitedNodes = [False] * self.numberofNodes
        path = []
        

    def eulerian_cycle(self):
        # Sprawdź warunek konieczny: każdy wierzchołek ma parzysty stopień
        for i in range(self.numberofNodes):
            degree = sum(self.matrixRepresentation[i])
            if degree % 2 != 0:
                print("Graf nie ma cyklu Eulera (nie wszystkie stopnie są parzyste).")
                return None

        # Skopiuj macierz, by nie modyfikować oryginału
        graph_copy = [row[:] for row in self.matrixRepresentation]
        stack = [0]  # Zaczynamy od wierzchołka 1 (indeks 0)
        path = []

        while stack:
            v = stack[-1]
            found = False
            for u in range(self.numberofNodes):
                if graph_copy[v][u]:
                    # Usuwamy krawędź
                    graph_copy[v][u] = 0
                    graph_copy[u][v] = 0
                    stack.append(u)
                    found = True
                    break
            if not found:
                path.append(stack.pop())

        path = [v + 1 for v in path[::-1]]  # Zamiana na numerację od 1
        print("Cykl Eulera:", path)
        return path    
    