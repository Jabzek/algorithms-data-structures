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
    print("Help \t \tShow this message")
    print("Print \t \tPrint the tree using Pre-order, In-order and Post-order")
    print("Remove \t \tRemove elements from the tree")
    print("Delete \t \tDelete the whole tree")
    print("Rebalance \tRebalance the tree")
    print("Create \t \tCreate a new tree")
    print("Export \t \tExport the tree to tickzpicture")
    print("Find \t \tFind the minimum and maximum element")
    print("Height \t \tHeight of the tree")
    print("Exit \t \tExits the program\n")


def menu(root):
    help()
    
    while True:
        choice = input("Wybierz jaką operację chcesz wykonać: ").lower()
        print()

        match choice:
            case "print":
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

            case "remove":
                if root is None:
                    print("Drzewo nie istnieje. Nie można usunąć elementów.\n")
                else:
                    l_delete = list(map(int, input("Podaj węzły do usunięcia: ").split()))
                    print()
                    for val in l_delete:
                        root = delete_node(root, val, is_avl)
            
            case "delete":
                root = delete_whole_tree_post_order(root)
                print("Całe drzewo zostało usunięte\n")

            case "create":
                main()

            case "export":
                print("Work in progress...\n")
            
            case "rebalance":
                if root is None:
                    print("Drzewo nie istnieje. Nie można zbalansować drzewa.\n")
                else:
                    root = dsw_balance(root)
                    print("Drzewo zostało zbalansowane\n")

            case "find":
                if root is None:
                    print("Drzewo nie istnieje. Nie można znaleźć elementów.\n")
                else:
                    min_v, l_min = minimum(root, [])
                    max_v, l_max = maximum(root, [])
                    print("Najmniejszy element:", min_v)
                    print("Przebyta droga:", l_min, end="\n\n")
                    print("Największy element:", max_v)
                    print("Przebyta droga:", l_max, end="\n\n")

            case "height":
                if root is None:
                    print("Drzewo nie istnieje. Nie można znaleźć wysokości.\n")
                else:
                    hgt = height(root)
                    print("Wysokość drzewa to:", hgt)    
                    print()
            
            case "help":
                help()
            
            case "exit":
                print("Zakończenie programu")
                exit()
            
            case _:
                print("Błędny wybór. Proszę wybrać ponownie.\n")

def main():
    global is_avl
    
    print("Wybierz jakie drzewo chcesz skonstruować: (BST, AVL)")
    
    while True:
        tree = input("Wybór: ").lower()
        if tree == "bst":
            is_avl = False
            print()
            print("Wybrano drzewo BST\n")
            break
        elif tree == "avl":
            is_avl = True
            print()
            print("Wybrano drzewo AVL\n")
            break
        else:
            print("Błędny wybór. Proszę wybrać odpowiednie drzewo.")       
    
    
    print("Wybierz sposób wprowadzenia danych:")
    print("1. Wprowadź liczby z klawiatury (Keyboard)")
    print("2. Wczytaj liczby z generatora (Generator)")
    print("3. Wczytaj liczby z pliku (File)")
    
    while True:
        l = input("Wybór: ").lower()
        if l == "keyboard " or l == "1":
            n = input_numbers()
            print()
            break
        elif l == "2" or l == "generator":
            n = [random.randint(0, 100) for _ in range(10)]
            print(f"Wygenerowane liczby: {n}\n")
            break
        elif l == "3" or l == "file":
            try:
                with open("numbers.txt", "r") as file:
                    n = list(map(int, file.read().split()))
                print(f"Wczytane liczby: {n}\n")
            except FileNotFoundError:
                print("Plik nie został znaleziony. Proszę spróbować ponownie.")
                continue
            break
        else:
            print("Błędny wybór. Proszę wybrać odpowiednią operacje.")
    
    if is_avl:
        n.sort()
        root = build_avl_tree(n)
        menu(root)
    else:
        root = bst_create(n)
        menu(root)


if __name__ == "__main__":
    main()

