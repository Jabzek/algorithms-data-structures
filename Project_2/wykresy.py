import csv
import matplotlib.pyplot as plt


def read_csv(file_path, start_row=43):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)

        for _ in range(start_row):
            next(reader)
        
        array_size = []
        create_time_bst = []
        create_time_avl = []
        search_time_bst = []
        search_time_avl = []
        in_order_time_bst = []
        in_order_time_avl = []
        dsw_time_bst = []
        count = 0

        for row in reader:
            count += 1
            
            if count <= 5:
                array_size.append(int(row[1]))
                create_time_bst.append(float(row[2]) * 1000)
                search_time_bst.append(float(row[3]) * 1000)
                in_order_time_bst.append(float(row[4]) * 1000)
                dsw_time_bst.append(float(row[5]) * 1000)
            else:
                create_time_avl.append(float(row[2]) * 1000)
                search_time_avl.append(float(row[3]) * 1000)
                in_order_time_avl.append(float(row[4]) * 1000)
                
    return (array_size, create_time_bst, create_time_avl, search_time_bst, search_time_avl, in_order_time_bst, in_order_time_avl, dsw_time_bst)


def plot(array_size, create_time_bst, create_time_avl, search_time_bst, search_time_avl, in_order_time_bst, in_order_time_avl, dsw_time_bst):
    
    bst_oper = (create_time_bst, search_time_bst, in_order_time_bst, dsw_time_bst)
    avl_oper = (create_time_avl, search_time_avl, in_order_time_avl)    
    titles = ("Tworzenie drzew", "Wyszukanie min/max", "Wypisanie In-Order", "Równoważenie drzewa BST")
    file_names = ("create_time", "search_time", "in_order_time", "dsw_time")
    label_bst = ("BST Create Time", "BST Search Time", "BST In-Order Time")
    label_avl = ("AVL Create Time", "AVL Search Time", "AVL In-Order Time")

    for el in range(4):
        plt.figure()
        if el == 3:
            plt.plot(array_size, bst_oper[3], label='DSW Time', color='blue')
        else:
            plt.plot(array_size, bst_oper[el], label=label_bst[el], color='blue')
            plt.plot(array_size, avl_oper[el], label=label_avl[el], color='red')

        plt.title(titles[el])
        plt.xlabel("Rozmiar instancji")
        plt.ylabel("Czas [ms]")
        plt.legend()
        plt.grid()
        plt.savefig(f"wykresy/{file_names[el]}.png")
        plt.close()




array_size, create_time_bst, create_time_avl, search_time_bst, search_time_avl, in_order_time_bst, in_order_time_avl, dsw_time_bst = read_csv('measure.csv')
plot(array_size, create_time_bst, create_time_avl, search_time_bst, search_time_avl, in_order_time_bst, in_order_time_avl, dsw_time_bst)