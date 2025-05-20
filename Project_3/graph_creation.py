import random

class Graph:
    def generate_nodes(self, n):
        self.nodes = [i for i in range(n)]
        self.edges = []

    def add_edge(self, k):
        self.edges.append(k)



def generate():
    while True:
        try:
            n = int(input("Podaj liczbę wierzchołków: "))
            saturation = int(input("Podaj nasycenie grafu w %: "))
            if n <= 0 or saturation < 0 or saturation > 100:
                raise ValueError
            break
        except ValueError:
            print("Niepoprawne dane. Wpisz dane jeszcze raz.")

    graph = Graph()
    graph.generate_nodes(n)
    max_edges = n * (n - 1)
    num_edges = max_edges * saturation // 100
    i = 0

    while i <= num_edges: 
        a = random.randint(1, n, dtype=int)
        b = random.randint(1, n, dtype=int)
        k = (a, b)
        if a != b and k not in graph.edges:
            graph.add_edge(k)
            i += 1
            
def user_provided():
    n = int(input("Podaj liczbę wierzchołków: "))
