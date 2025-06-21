from itertools import combinations

def brute_force(capacity, numberofItems, itemValues, itemWeights):
    maxValue = 0
    bestCombination = []
    listofCombinations = []

    for length in range(1, numberofItems + 1):
        listofCombinations.append(combinations(range(numberofItems), length))

    print(listofCombinations)