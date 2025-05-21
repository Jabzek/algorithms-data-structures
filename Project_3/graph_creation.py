import random
from graph import Graph
            

def generate():
    while True:
        try:
            n = int(input("Podaj liczbę wierzchołków: "))
            saturation = int(input("Podaj nasycenie grafu w %: "))
            if n <= 0 or saturation <= 0 or saturation > 100:
                raise ValueError
            break
        except ValueError:
            print("Niepoprawne dane. Wpisz dane jeszcze raz.\n")

    graph = Graph()
    max_edges = n * (n - 1) // 2
    num_edges = max_edges * saturation // 100
    i = 0

    while i < num_edges: 
        a = random.randint(1, n)
        b = random.randint(1, n)
        
        if a > b:
            a, b = b, a
        k = (a, b)
        
        if a != b and k not in graph.edges:
            graph.add_edge(k)
            i += 1

    return graph, n
    
            
def user_provided():
    while True:
        try:    
            n = int(input("Podaj liczbę wierzchołków: "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Niepoprawne dane. Wpisz dane jeszcze raz.\n")
    
    graph = Graph()
    print("Przy każdym wierzchołku podaj listę jego następników.\n")
    idx = 1
    
    while idx <= n:
        try:
            l = list(map(int, input(f"Podaj następniki wierzchołka {idx} -> ").split()))
            if len(l) == 0:
                idx += 1
                continue
            if any(i > n or i < 1 for i in l):
                raise ValueError
            else:
                for i in l:
                    graph.add_edge((idx, i))
        except ValueError:
            print("Niepoprawny wierzchołek, wpisz dane jeszcze raz.")
            continue
        idx += 1

    return graph, n
