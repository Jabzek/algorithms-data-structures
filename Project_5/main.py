from data import data_provide


def main():
    while True:
        try:
            action = input("W jaki sposób chcesz uzyskać dane? (z pliku (File) / ręcznie (Manual)): ").strip().lower()
            if action != "file" and action != "manual":
                raise ValueError
            break
        except ValueError:
                print("Nieprawidłowy wybór. Wybierz 'file' lub 'manual'.\n")    
            
    if action == "file":
        filename = input("Podaj ścieżkę do pliku CSV: ").strip()

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

    



if __name__ == "__main__":
    main()