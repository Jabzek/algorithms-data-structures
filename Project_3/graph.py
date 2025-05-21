import copy

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
    
    def g_print(graph, representation, n):
        if representation == "matrix":
            l_matrix = []
            l_matrix.append("  | " + " ".join([str(i) for i in range(1, n+1)]))
            l_matrix.append("--+" + "-" * (n * 2))

            for row in l_matrix:
                print(row)