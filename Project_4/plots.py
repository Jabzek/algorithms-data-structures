import matplotlib.pyplot as plt
import csv
import os


def read_data():
    with open("measure.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        hamiltonianTime = []
        eulerianTime = []
        numberofNodes1 = []
        nonhamiltonianTime = []
        numberofNodes2 = []

        for row in reader:
            if row[0] == "Hamiltonian":
                numberofNodes1.append(int(row[1]))
                hamiltonianTime.append(float(row[2]))
                eulerianTime.append(float(row[3]))
            else:
                numberofNodes2.append(int(row[1]))
                nonhamiltonianTime.append(float(row[2]))

    return hamiltonianTime, eulerianTime, numberofNodes1, nonhamiltonianTime, numberofNodes2


def plot_create(hamiltonianTime, eulerianTime, numberofNodes1, nonhamiltonianTime, numberofNodes2):
    directory = os.path.dirname(__file__)
    dirname = os.path.join(directory, "Plots")
    
    
    numberofNodes = (numberofNodes1, numberofNodes1, numberofNodes2)
    alghorithmTime = (hamiltonianTime, eulerianTime, nonhamiltonianTime)
    titles = ("Finding Hamiltonian Cycle", "Finding Eulerian Cycle", "Finding Hamiltonian Cycle")
    labels = ("Hamiltonian Cycle Graph", "Eulerian Cycle", "Non-Hamiltonian Cycle Graph")
    file_names = ("hamiltonian_cycle", "eulerian_cycle", "non_hamiltonian_cycle")

    for el in range(3):
        plt.figure()
        plt.plot(numberofNodes[el], alghorithmTime[el], label=labels[el], color='red')
        plt.xlabel("Number of Nodes")
        plt.ylabel("Time (seconds)")
        plt.title(titles[el])
        plt.legend()
        plt.grid()
        if el != 1:
            plt.yscale("log")
        plt.savefig(os.path.join(dirname, f"{file_names[el]}.png"))
        plt.close()

    print("Wykonano wykresy i zapisano do katalogu Plots")


if __name__ == "__main__":
    hamiltonianTime, eulerianTime, numberofNodes1, nonhamiltonianTime, numberofNodes2 = read_data()
    plot_create(hamiltonianTime, eulerianTime, numberofNodes1, nonhamiltonianTime, numberofNodes2)