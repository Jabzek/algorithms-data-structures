from Insertion_sort import insertion_sort
from Selection_sort import selection_sort
from Shell_sort import shell_sort
from generate import generate_all_arrays, sizes

def main():
    print("Enter a name of algorithm you want to perform. Choose from the following:\n1. Insertion Sort\n2. Selection Sort\n3. Shell Sort")
    
    while True:
        algorithm = input().lower()
        dict_arrays = generate_all_arrays(sizes)
        
        if algorithm in ["insertion sort", "selection sort", "shell sort"]:
            for el in dict_arrays.values():
                for name, arr in el:
                    if algorithm == "insertion sort":
                        sorted_array = insertion_sort(arr.copy())
                        print(f"Array before sorting: {arr}.\nType of input array: {name}.\nArray after using Insertion sort: {sorted_array}")
                        quit_function()  
                    elif algorithm == "selection sort":
                        sorted_array = selection_sort(arr.copy())
                        print(f"Array before sorting: {arr}.\nType of input array: {name}.\nArray after using Selection sort: {sorted_array}")
                        quit_function()
                    elif algorithm == "shell sort":
                        sorted_array = shell_sort(arr.copy())
                        print(f"Array before sorting: {arr}.\nType of input array: {name}.\nArray after using Shell sort: {sorted_array}")
                        quit_function()
        else:
            print("Invalid input. Try again.")

def quit_function():
    print("Do you want to quit? (yes/no)")
    while True:
        answer = input().lower()
        if answer == "yes":
            quit()
        elif answer == "no":
            return
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()