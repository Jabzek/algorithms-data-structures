import csv

def data_provide(filename):
    while True:
        try: 
            capacity = float(input("Podaj pojemność plecaka: "))
            if capacity <= 0:
                raise ValueError
            break
        except ValueError:
            print("Pojemność musi być liczbą większą od zera. Spróbuj ponownie.")
    
    while True:
        try:
            numberofItems = int(input("Podaj liczbę przedmiotów: "))
            if numberofItems <= 0:
                raise ValueError
            break
        except ValueError:
            print("Liczba przedmiotów musi być większa od zera. Spróbuj ponownie.")

    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([capacity])
        writer.writerow([numberofItems])
    
    for el in range(numberofItems):
        while True:
            try: 
                itemWeight = float(input(f"Podaj wagę przedmiotu {el + 1}: "))
                if itemWeight <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Waga musi być większa od zera. Spróbuj ponownie.")

        while True:
            try:
                itemValue = float(input(f"Podaj wartość przedmiotu {el + 1}: "))
                if itemValue <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Wartość musi być większa od zera. Spróbuj ponownie.")

        with open(filename, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow((itemValue, itemWeight))
        
    print(f"Dane zostały zapisane do pliku {filename}.")

def data_read(filename):
    itemValeus = []
    itemWeights = []

    with open(filename, "r") as file:
        reader = csv.reader(file)        
        for el in range(2):
            if el == 0:
                capacity = float(next(reader)[0])
            else:
                numberofItems = int(next(reader)[0])

        for row in reader:
            itemValeus.append(float(row[0]))
            itemWeights.append(float(row[1]))
    
    return capacity, numberofItems, itemValeus, itemWeights