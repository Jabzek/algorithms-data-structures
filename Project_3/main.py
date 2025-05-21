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

    print("Wybierz reprezentację grafu:", end=" ")
    while True:
        a = input().lower()
        if a == "s":
            graph.show_as_set()
            break
        elif a == "l":
            graph.show_as_list()
            break
        elif a == "m":
            graph.show_as_matrix()
            break
        else:
            print("Niepoprawna komenda. Wybierz 's', 'l' lub 'm'.")




if __name__ == "__main__":
    main()