import csv 
import os
import matplotlib.pyplot as plt


def read_csv():
    script_dir = os.path.dirname(__file__) #Get the directory of the script
    filename = os.path.join(script_dir, "measure.csv") #Saving in the same directory as the script

    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        array_size = []
        search_time_matrix = []
        search_time_list = []
        search_time_table = []
        kahn_time_matrix = []
        kahn_time_list = []
        kahn_time_table = []
        tarjan_time_matrix = []
        tarjan_time_list = []
        tarjan_time_table = []

        for row in reader:
            if int(row[0]) not in array_size:
                array_size.append(int(row[0]))

            if row[1] == "matrix":
                search_time_matrix.append(float(row[2]))
                kahn_time_matrix.append(float(row[3]))
                tarjan_time_matrix.append(float(row[4]))
            elif row[1] == "list":
                search_time_list.append(float(row[2]))
                kahn_time_list.append(float(row[3]))
                tarjan_time_list.append(float(row[4]))
            elif row[1] == "table":
                search_time_table.append(float(row[2]))
                kahn_time_table.append(float(row[3]))
                tarjan_time_table.append(float(row[4]))

    plot(array_size, search_time_matrix, search_time_list, search_time_table, kahn_time_matrix, kahn_time_list, kahn_time_table, tarjan_time_matrix, tarjan_time_list, tarjan_time_table)


def plot(array_size, search_time_matrix, search_time_list, search_time_table, kahn_time_matrix, kahn_time_list, kahn_time_table, tarjan_time_matrix, tarjan_time_list, tarjan_time_table):
    script_dir = os.path.dirname(__file__)
    output_dir = os.path.join(script_dir, "Plots")
    
    matrix_oprtions = (search_time_matrix, kahn_time_matrix, tarjan_time_matrix)
    list_oprtions = (search_time_list, kahn_time_list, tarjan_time_list)
    table_oprtions = (search_time_table, kahn_time_table, tarjan_time_table)
    titles = ("Finding edge", "Kahn algorithm", "Tarjan algorithm")
    file_names = ("search_time", "kahn_time", "tarjan_time")
    label_matrix = ("Matrix Search Time", "Matrix Kahn Time", "Matrix Tarjan Time")
    label_list = ("List Search Time", "List Kahn Time", "List Tarjan Time")
    label_table = ("Table Search Time", "Table Kahn Time", "Table Tarjan Time")

    for el in range(3):
        plt.figure()
        plt.plot(array_size, matrix_oprtions[el], label=label_matrix[el], color='blue')
        plt.plot(array_size, list_oprtions[el], label=label_list[el], color='red')
        plt.plot(array_size, table_oprtions[el], label=label_table[el], color='green')
        plt.title(titles[el])
        plt.xlabel("Rozmiar instancji")
        plt.ylabel("Czas [s]")
        plt.yscale("log")
        plt.legend()
        plt.grid()
        plt.savefig(os.path.join(output_dir, f"{file_names[el]}.png"))
        plt.close()

    print("Wykonano wykresy i zapisano do katalogu Plots")

if __name__ == "__main__":
    read_csv()