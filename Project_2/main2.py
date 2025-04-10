import random
from bst import bst_create

def input_numbers():
    while True:
        print("Wprowadź liczby całkowite: ", end="")
        try:
            n = list(map(int, input().split()))
            break
        except ValueError:
            print("Błędne dane. Proszę wprowadzić liczby całkowite.")
    return n   

def main():
    print("Wybierz sposób wprowadzenia danych:")
    print("1. Wprowadź liczby z klawiatury")
    print("2. Wczytaj liczby z generatora")
    
    while True:
        l = input("Wybór: ")
        if l == "1":
            n = input_numbers()
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
            bst_create(n)
            break
        elif tree == "2" or tree == "avl":
            break
        else:
            print("Błędny wybór. Proszę wybrać odpowiednie drzewo.")        
    

if __name__ == "__main__":
    main()

