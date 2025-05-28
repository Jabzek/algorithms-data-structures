import argparse
from graph_create import create_graph

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






if __name__ == "__main__":
    main()