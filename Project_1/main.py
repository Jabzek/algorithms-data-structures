from Insertion_sort import insertion_sort
from Selection_sort import selection_sort
from Shell_sort import shell_sort
from generate import generate_all_arrays, sizes
from heap_sort import heap_sort
from quick_sort_left_pivot import quick_sort_left_pivot
from quick_sort_random_pivot import quick_sort_random_pivot

def main():
    print("Enter a name of algorithm you want to perform. Choose from the following:\n1. Insertion Sort\n2. Selection Sort\n3. Shell Sort\n4. Heap Sort\n5. Quick Sort left pivot\n6. Quick Sort random pivot")
    
    while True:
        algorithm = input().lower().replace(" ", "")
        dict_arrays = generate_all_arrays(sizes)
        l = ["insertionsort", "selectionsort", "shellsort", "heapsort", "quicksortleftpivot", "quicksortrandompivot"]

        if algorithm in l:
            for el in dict_arrays.values():
                for name, arr in el.items():
                    if algorithm == "insertionsort":
                        sorted_array = insertion_sort(arr.copy())
                        print(f"\nArray before sorting: {arr}\nType of input array: {name}\nArray after using Insertion sort: {sorted_array}")
                        quit_function()  
                        
                    elif algorithm == "selectionsort":
                        sorted_array = selection_sort(arr.copy())
                        print(f"\nArray before sorting: {arr}\nType of input array: {name}\nArray after using Selection sort: {sorted_array}")
                        quit_function()
                    
                    elif algorithm == "shellsort":
                        sorted_array = shell_sort(arr.copy())
                        print(f"\nArray before sorting: {arr}\nType of input array: {name}\nArray after using Shell sort: {sorted_array}")
                        quit_function()
                    
                    elif algorithm == "heapsort":
                        sorted_array = heap_sort(arr.copy())
                        print(f"\nArray before sorting: {arr}\nType of input array: {name}\nArray after using Heap sort: {sorted_array}")
                        quit_function()

                    elif algorithm == "quicksortleftpivot":
                        sorted_array = quick_sort_left_pivot(arr.copy(), 0, len(arr) - 1)
                        print(f"\nArray before sorting: {arr}\nType of input array: {name}\nArray after using Quick sort: {sorted_array}")
                        quit_function()

                    elif algorithm == "quicksortrandompivot":
                        sorted_array = quick_sort_random_pivot(arr.copy(), 0, len(arr) - 1)
                        print(f"\nArray before sorting: {arr}\nType of input array: {name}\nArray after using Quick sort: {sorted_array}")
                        quit_function()
            break
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