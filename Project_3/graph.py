import copy
import time

class Graph:
    def __init__(self):
        self.edges = []


    def add_edge(self, k):
        self.edges.append(k)    


    def show_matrix(self, n):
        self.matrix = [[0] * n for _ in range(n)]
        for el in self.edges:
            a, b = el
            self.matrix[a-1][b-1] = 1


    def show_list(self, n):
        self.list = [[] for _ in range(n)]
        for el in self.edges:
            a, b = el
            self.list[a-1].append(b)
            

    def show_table(self):
        self.table = copy.deepcopy(self.edges)
        self.table.sort(key=lambda x: x[0])
    

    def g_print(self, representation, n):
        if representation == "matrix":
            l_matrix = []
            l_matrix.append("  | " + " ".join([str(i) for i in range(1, n+1)]))
            l_matrix.append("--+" + "-" * (n * 2))

            for el in range(1, n+1):
                l_matrix.append(f"{el} | " + " ".join([str(self.matrix[el-1][i]) for i in range(n)]))       
            
            for row in l_matrix:
                print(row)
            print()
        elif representation == "list":
            idx = 1
            for el in self.list:
                print(f"{idx}: " + " ".join(str(i) for i in el))
                idx += 1
            print()
        elif representation == "table":
            for el in self.table:
                print(f"{el[0]} -> {el[1]}")
            print()


    def find(self, representation, n):
        print("Podaj wierzchołki krawędzi")
        try:
            a = int(input("from -> "))
            b = int(input("to -> "))
            if a <= 0 or b <= 0 or a > n or b > n:
                raise ValueError 
        except ValueError:
            print("Podano nieistniejące wierzchołki.\n")
            return
                
        if representation == "matrix":
            if self.matrix[a-1][b-1] == 1:
                print("Krawędź istnieje w grafie")
            else:
                print("Krawędź nie istnieje w grafie")
        elif representation == "list":
            if b in self.list[a-1]:
                print("Krawędź istnieje w grafie")
            else:
                print("Krawędź nie istnieje w grafie")
        elif representation == "table":
            if (a, b) in self.table:
                print("Krawędź istnieje w grafie")
            else:
                print("Krawędź nie istnieje w grafie")
        print()


    def kahn(self, representation, n):
        self.kahn_list = []
        in_degree = [0] * n
        
        if representation == "matrix":
            for i in range(n):
                for j in range(n):
                    if self.matrix[i][j] == 1:
                        in_degree[j] += 1
            
        elif representation == "list":
            for i in range(n):
                for el in self.list[i]:
                    in_degree[el-1] += 1
        
        elif representation == "table":
            for el in self.table:
                in_degree[el[1]-1] += 1
        
        queue = []
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i + 1)

        while queue:
            node = queue.pop(0)
            self.kahn_list.append(node)

            if representation == "matrix":
                for el in range(n):
                    if self.matrix[node-1][el] == 1:
                        in_degree[el] -= 1
                        if in_degree[el] == 0:
                            queue.append(el + 1)
            elif representation == "list":
                for el in self.list[node-1]:
                    in_degree[el-1] -= 1
                    if in_degree[el-1] == 0:
                        queue.append(el)
            elif representation == "table":  
                for el in self.table:
                    if el[0] == node:
                        in_degree[el[1]-1] -= 1
                        if in_degree[el[1]-1] == 0:
                            queue.append(el[1])
        
        if len(self.kahn_list) != n:
            print("Graf nie jest acykliczny")
        else:
            print("Kolejność topologiczna grafu: " + " ".join(str(i) for i in self.kahn_list))