import os
import csv
import random
from graph_creation import generate

SATURATION = 70


def locate(n, representation, graph):
    a = random.randint(1, n)
    b = random.randint(1, n)
    elapsed_time = graph.find(representation, n, a, b, measurements=True)
    return elapsed_time


def main(n, saturation):
    script_dir = os.path.dirname(__file__) #Get the directory of the script
    filename = os.path.join(script_dir, "measure.csv") #Saving in the same directory as the script
    
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(("Number of nodes", "Representation", "Search edge", "Kahn algorithm", "Tarjan algorithm"))
    
    for el in n:
        graph, _ = generate(saturation, el, measurements=True)
        for representation in ["matrix", "list", "table"]:
            if representation == "matrix":
                graph.show_matrix(el)
            elif representation == "list":
                graph.show_list(el)
            else: 
                graph.show_table()

            time_search = locate(el, representation, graph)
            time_kahn = graph.kahn(representation, el, measurements=True)
            time_tarjan = graph.tarjan(representation, el, measurements=True)

            with open(filename, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow((el, representation, time_search, time_kahn, time_tarjan))
            print(f"Wykonano pomiary dla {representation}")

        print(f"Pomiary dla {el} wierzchołków zapisano do measure.csv")
    
    return filename

n = [256, 512, 840, 1024, 1300]

if __name__ == "__main__":
    main(n, SATURATION)
    print("Wykonano pomiary i zapisano do measure.csv")
