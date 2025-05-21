import argparse
from graph_creation import generate, user_provided
from graph_operations import print_graph

def help():
    print("Help \t\t\t Pokazuje tę wiadomość")
    print("Print \t\t\t Wypisuje graf w wybranej reprezentacji")
    print("Find \t\t\t Sprawdza czy podana krawędź istnieje w grafie")
    print("Breath-first search \t Przechodzenie grafu wszerz (BFS)")
    print("Depth-first search \t Przechodzenie grafu w głąb (DFS)")
    print("Kahn \t\t\t Algorytm Kahn'a")
    print("Tarjan \t\t\t Algorytm Tarjan'a")
    print("Exit \t\t\t Kończy program\n")


def main():
    parser = argparse.ArgumentParser(description="Generowanie grafu.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--generate", action="store_true", help="Generuj graf losowo")
    group.add_argument("--user-provided", action="store_true", help="Wczytaj graf od użytkownika")
    args = parser.parse_args()

    if args.generate:
        graph, n = generate()
    elif args.user_provided:
        graph, n = user_provided()
    else:
        print("Niepoprawna komenda. Użyj '--generate' lub '--user_provided'.")

    print("Wybierz reprezentację grafu (matrix/list/table):", end=" ")
    while True:
        representation = input().lower()

        if representation == "matrix":
            graph.show_matrix(n)
            break
        elif representation == "list":
            graph.show_list(n)
            break
        elif representation == "table":
            graph.show_table(n)
            break
        else:
            print("Niepoprawna komenda. Wybierz matrix, list lub table.")

    print("Jaką operację chcesz wykonać?\n")
    help()    
    
    while True:
        operation = input("action -> ").lower()
        match operation:
            case "help":
                help()
            case "exit":
                print("Koniec programu.")
                exit()
            case "print":
                print_graph(graph, representation, n)                  




if __name__ == "__main__":
    main()