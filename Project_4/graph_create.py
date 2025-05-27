
def hamilton():
    while True:
        try:
            numberofNodes = int(input("Podaj liczbę wierzchołków: "))
            saturation = int(input("Podaj stopień nasycenia grafu (30/70): "))
            if numberofNodes <= 0 or saturation != 30 and saturation != 70:
                raise ValueError
            break
        except ValueError:
            print("Niepoprawne dane. Wpisz dane jeszcze raz.\n")

    




def non_hamilton():
    pass