import argparse
from graph_creation import generate, user_provided



def main():
    parser = argparse.ArgumentParser(description="Generowanie grafu.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--generate", action="store_true", help="Generuj graf losowo")
    group.add_argument("--user-provided", action="store_true", help="Wczytaj graf od użytkownika")
    args = parser.parse_args()

    if args.generate:
        graph = generate()
    elif args.user_provided:
        graph = user_provided()
    else:
        print("Niepoprawna komenda. Użyj '--generate' lub '--user_provided'.")

    print(graph.edges)


if __name__ == "__main__":
    main()