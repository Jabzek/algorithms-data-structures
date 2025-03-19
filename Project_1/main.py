def main():
    print("Enter a name of algorithm you want to perform. Choose from the following:\n1. Insertion Sort\n2. Selection Sort\n3. Shell Sort")
    while True:
        algorithm = input().lower()
        if algorithm == "insertion sort":
            print("Insertion Sort")
            break
        elif algorithm == "selection sort":
            print("Selection Sort")
            break
        elif algorithm == "shell sort":
            print("Shell Sort")
            break
        else:
            print("Invalid input. Try again.")







main()