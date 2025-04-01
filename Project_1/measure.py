import csv
import os
import math
from time import time
from generate import generate_all_arrays, sizes
from Insertion_sort import insertion_sort
from Selection_sort import selection_sort
from Shell_sort import shell_sort
from heap_sort import heap_sort
from quick_sort_left_pivot import quick_sort_left_pivot
from quick_sort_random_pivot import quick_sort_random_pivot


def creating_file(res):
    script_dir = os.path.dirname(__file__) #Get the directory of the script
    filename = os.path.join(script_dir, "measurements.csv") #Saving in the same directory as the script
    headers = ["Algorithm", "Array Type", "Array Size", "Time (seconds)"]
    
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(res)
            
def to_superscript(num):
    superscript_map = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    return str(num).translate(superscript_map)


res = []
arrays = generate_all_arrays(sizes)
algorithms = {
    "Insertion_sort": insertion_sort,
    "Selection_sort": selection_sort,
    "Shell_sort": shell_sort,
    "Heap_sort": heap_sort,
    "Quick_sort_left_pivot": quick_sort_left_pivot,
    "Quick_sort_random_pivot": quick_sort_random_pivot
}

for name, algorithm in algorithms.items():
    print("Running", name)
    for array_dict in arrays.values():
        for typ, array in array_dict.items():
            len_arr = len(array)
            size = int(math.log2(len_arr))
            arr_size = f"2{to_superscript(size)}"
            
            if name == "Quick_sort_left_pivot" or name == "Quick_sort_random_pivot":
                start_time = time()
                algorithm(array.copy(), 0, len_arr - 1)
                end_time = time()
            else:
                start_time = time()
                algorithm(array.copy())
                end_time = time()

            elapsed_time = end_time - start_time
            res.append((name, typ, arr_size, elapsed_time))

creating_file(res)


