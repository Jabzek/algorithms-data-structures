import argparse
from graph_create import create_graph



def help_messages():
    print("Help \t\t Pokazuje dostępne komendy.")
    print("Print \t\t Wypisuje graf.")
    print("Euler \t\t Znajduje cykl Eulera w grafie.")
    print("Hamilton \t Znajduje cykl Hamiltona w grafie.")
    print("Export \t\t Eksportuje graf do tickzpicture.")
    print("Exit \t\t Kończy program.")

def main():
    parser = argparse.ArgumentParser(description="Generowanie grafu.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--hamilton", action="store_true", help="Utwórz graf Hamiltonowski")
    group.add_argument("--non-hamilton", action="store_true", help="Utwórz graf nie-Hamiltonowski")
    args = parser.parse_args()

    if args.hamilton:
        graph = create_graph(hamiltonGraph=True)
    elif args.non_hamilton:
        graph = create_graph(hamiltonGraph=False)
    else:
        print("Niepoprawna komenda. Użyj '--hamilton' lub '--non-hamilton'.")

    print("Graf został utworzony. Wybierz operację do wykonania na grafie:\n")
    help_messages()

    while True:
        command = input("Wprowadź komendę: ").strip().lower()
        print()
        match command:
            case "help":
                help_messages()
            case "print":
                graph.show_graph()
            case "euler":
                graph.eulerian_cycle()
            case "hamilton":
                graph.hamiltonian_cycle()
            case "export":
                graph.export_to_tickz()
            case "exit":
                break
            case _:
                print("Nieznana komenda. Spróbuj ponownie.")

if __name__ == "__main__":
    main()