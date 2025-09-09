import time
import numpy as np
import os
import csv

def gen_data(n):
    data = []
    for i in n:
        data.append(np.random.randint(0, 5000, i, dtype=int))
    return data


def tree_measure(data, filename, tree):
    from bst import bst_create 
    from avl_builder import build_avl_tree
    from tree_ops import in_order, dsw_balance, minimum_val, maximum


    for i in data:
        len_data = len(i)
        
        for _ in range(4):  
            
            if tree == "BST":
                c_time = time.time()
                root = bst_create(i)
                c_end = time.time()
            elif tree == "AVL":
                c_time = time.time()
                root = build_avl_tree(i)
                c_end = time.time()
            
            s1_time = time.time()
            minimum_val(root)
            s1_end = time.time()

            s2_time = time.time()
            maximum(root, [])
            s2_end = time.time()

            in_order_time = time.time()
            in_order(root)
            in_order_end = time.time()

            if tree == "BST":
                dsw_time = time.time()
                dsw_balance(root)
                dsw_end = time.time()

            with open(filename, mode="a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow((tree, len_data, c_end - c_time, s1_end - s1_time, s2_end - s2_time, in_order_end - in_order_time, dsw_end - dsw_time if tree == "BST" else ""))

def average(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        create_times = []
        search_times_min = []
        search_times_max = []
        in_order_times = []
        dsw_times = []
        max_row = 40
        rows = 0

        for row in reader:
            rows += 1
            if rows > max_row:
                break
            
            name = row[0]
            size = row[1]
            create_times.append(float(row[2]))
            search_times_min.append(float(row[3]))
            search_times_max.append(float(row[4]))
            in_order_times.append(float(row[5]))
            
            if name == "BST":
                dsw_times.append(float(row[6]))
            
            if len(create_times) == 4:
                avg_create = sum(create_times) / len(create_times)
                avg_in_order = sum(in_order_times) / len(in_order_times)
                avg_search = (sum(search_times_max) + sum(search_times_min)) / (len(search_times_max) + len(search_times_min))

                if name == "BST":
                    avg_dsw = sum(dsw_times) / len(dsw_times)
                
                with open(filename, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow((name, size, avg_create, avg_search, avg_in_order, avg_dsw if name == "BST" else ""))
                
                create_times = []
                search_times_min = []
                search_times_max = []
                in_order_times = []
                dsw_times = []

def main(n):            
    data = gen_data(n)
    script_dir = os.path.dirname(__file__) #Get the directory of the script
    filename = os.path.join(script_dir, "measure.csv") #Saving in the same directory as the script

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(("Tree", "Array Size", "Create Time", "Search Time Min", "Search Time Max", "In-order Traversal", "Balance (in BST)"))

    tree_measure(data, filename, tree="BST")
    tree_measure(data, filename, tree="AVL")

    print("\n")
    print("Pomiary zostały zapisane w pliku measure.csv, czy chcesz obliczyć średnie czasy dla każdej wielkości listy z danego drzewa?")
    answer = input("Tak, Nie: ").lower()

    if answer == "nie":
        exit()
    elif answer == "tak":
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(("", "", "", "", "", "", ""))
            writer.writerow(("Tree", "Array Size", "Create Time", "Search Time", "In-order Traversal", "Balance (in BST)"))
        average(filename)


n = [2 ** i for i in range(12, 17)]

if __name__ == "__main__":
    main(n)