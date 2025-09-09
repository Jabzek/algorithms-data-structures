from itertools import combinations

def brute_force(capacity, numberofItems, itemValues, itemWeights):
    maxValue = 0
    listofCombinations = []

    for length in range(1, numberofItems + 1):
        listofCombinations.extend(list(combinations(range(numberofItems), length)))

    for combination in listofCombinations:
        totalWeight = sum(itemWeights[i] for i in combination)
        totalValue = sum(itemValues[i] for i in combination)

        if totalWeight <= capacity and totalValue > maxValue:
            maxValue = totalValue
            bestCombination = combination

    print(f"Najlepsza kombinacja przedmiotów; {", ".join(str(i + 1) for i in bestCombination)}")
    print(f"Łączna wartość przedmiotów: {maxValue}")