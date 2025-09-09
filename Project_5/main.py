from data import data_provide, data_read
from bruteforce import brute_force
from dynamic_programming import dynamic_programming

def main():
    while True:
        try:
            action = input("W jaki sposób chcesz uzyskać dane? (z pliku data.csv (File) / ręcznie (Manual)): ").strip().lower()
            if action != "file" and action != "manual":
                raise ValueError
            break
        except ValueError:
                print("Nieprawidłowy wybór. Wybierz 'file' lub 'manual'.\n")    
            
    if action == "file":
        filename = "data.csv"
        capacity, numberofItems, itemValues, itemWeights = data_read(filename)
        print(f"Pojemność plecaka: {capacity}")
        print(f"Liczba przedmiotów: {numberofItems}")
        print(f"Wartości przedmiotów: {", ".join(str(value) for value in itemValues)}")
        print(f"Wagi przedmiotów: {", ".join(str(weight) for weight in itemWeights)}")
        print()
    elif action == "manual":
        while True:
            try:
                filename = input("Podaj nazwę pliku do zapisu danych (name.csv): ").strip()
                if not filename.endswith(".csv"):
                    raise ValueError
                print()
                break
            except ValueError:
                print("Plik musi mieć rozszerzenie .csv. Spróbuj ponownie.\n")
        data_provide(filename)
        capacity, numberofItems, itemValues, itemWeights = data_read(filename)

    while True:
        try:
            algorithm = input("Jaki algorytm chcesz użyć? (Brute Force / Dynamic Programming): ").strip().lower()
            if algorithm not in ["brute force", "dynamic programming"]:
                raise ValueError
            break
        except ValueError:
            print("Nieprawidłowy wybór. Wybierz Brute Force lub Dynamic Programming.\n")

    if algorithm == "brute force":
        brute_force(capacity, numberofItems, itemValues, itemWeights)
    elif algorithm == "dynamic programming":
        dynamic_programming(capacity, numberofItems, itemValues, itemWeights)

if __name__ == "__main__":
    main()