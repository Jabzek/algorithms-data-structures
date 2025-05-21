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

    def show_table(self, n):
        self.table = copy.deepcopy(self.edges)
        self.table.sort(key=lambda x: x[0])
            