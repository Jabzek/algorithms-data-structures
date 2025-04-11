import random
from bst import bst_create
from avl_builder import build_avl_tree
from tree_ops import *

def input_numbers():
    while True:
        print("Wprowadź liczby całkowite: ", end="")
        try:
            n = list(map(int, input().split()))
            break
        except ValueError:
            print("Błędne dane. Proszę wprowadzić liczby całkowite.")
    return n   

def help():
    print("1. Wypisz drzewo w porządku pre-order, in-order, post-order")
    print("2. Usuń elementy z drzewa")
    print("3. Usuń całe drzewo")
    print("4. Utwórz nowe drzewo (BST lub AVL)")
    print("5. Eksportuj drzewo do tickzpicture")
    print("6. Balansowanie drzewa")
    print("7. Wyszukiwanie najwiekszego i najmniejszego elementu")
    print("8. Wysokość drzewa")
    print("9. Help")
    print("10. Zakończenie programu\n")


def menu(root):
    help()
    
    while True:
        choice = input("Wybierz jaką operację chcesz wykonać: ").lower()
        print()

        match choice:
            case "1":
                if root is None:
                    print("Drzewo nie istnieje. Nie można wypisać elementów.\n")
                else:
                    print("Drzewo w porządku pre-order: ", end="")
                    pre_order(root)
                    print()
                    
                    print("Drzewo w porządku in-order: ", end="")
                    in_order(root)
                    print()
                    
                    print("Drzewo w porządku post-order: ", end="")
                    post_order(root)
                    print("\n")

            case "2":
                if root is None:
                    print("Drzewo nie istnieje. Nie można usunąć elementów.\n")
                else:
                    l_delete = list(map(int, input("Podaj węzły do usunięcia: ").split()))
                    print()
                    for val in l_delete:
                        root = delete_node(root, val, is_avl)
            
            case "3":
                root = delete_whole_tree_post_order(root)
                print("Całe drzewo zostało usunięte\n")

            case "4":
                main()

            case "5":
                print("Work in progress...\n")
            
            case "6":
                if root is None:
                    print("Drzewo nie istnieje. Nie można zbalansować drzewa.\n")
                else:
                    root = dsw_balance(root)
                    print("Drzewo zostało zbalansowane\n")

            case "7":
                if root is None:
                    print("Drzewo nie istnieje. Nie można znaleźć elementów.\n")
                else:
                    min_v, l_min = minimum(root, [])
                    max_v, l_max = maximum(root, [])
                    print("Najmniejszy element:", min_v)
                    print("Przebyta droga:", l_min, end="\n\n")
                    print("Największy element:", max_v)
                    print("Przebyta droga:", l_max, end="\n\n")

            case "8":
                if root is None:
                    print("Drzewo nie istnieje. Nie można znaleźć wysokości.\n")
                else:
                    hgt = height(root)
                    print("Wysokość drzewa to:", hgt)    
                    print()
            
            case "9" | "help":
                help()
            
            case "10":
                print("Zakończenie programu")
                exit()
            
            case _:
                print("Błędny wybór. Proszę wybrać ponownie.\n")

def main():
    global is_avl
    print("Wybierz sposób wprowadzenia danych:")
    print("1. Wprowadź liczby z klawiatury")
    print("2. Wczytaj liczby z generatora")
    
    while True:
        l = input("Wybór: ")
        if l == "1":
            n = input_numbers()
            print()
            break
        elif l == "2":
            n = [random.randint(0, 100) for _ in range(10)]
            print(f"Wygenerowane liczby: {n}\n")
            break
        else:
            print("Błędny wybór. Proszę wybrać 1 lub 2.")
    
    print("Wybierz jakie drzewo chcesz skonstruować: (1. BST, 2. AVL)")
    
    while True:
        tree = input("Wybór: ").lower()
        if tree == "1" or tree == "bst":
            is_avl = False
            print()
            print("Wybrano drzewo BST\n")
            root = bst_create(n)
            menu(root)
            break
        elif tree == "2" or tree == "avl":
            is_avl = True
            print()
            print("Wybrano drzewo AVL\n")
            n.sort()
            root = build_avl_tree(n)
            menu(root)
            break
        else:
            print("Błędny wybór. Proszę wybrać odpowiednie drzewo.")        
    

if __name__ == "__main__":
    main()

