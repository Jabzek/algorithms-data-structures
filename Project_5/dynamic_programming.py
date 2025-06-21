def dynamic_programming(capacity, numberofItems, itemValues, itemWeights):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(numberofItems + 1)]

    for i in range(1, numberofItems + 1):
        for w in range(capacity + 1):
            if itemWeights[i - 1] <= w:
                dp[i][w] = max(
                    itemValues[i - 1] + dp[i - 1][w - itemWeights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    w = capacity
    chosen_items = []
    for i in range(numberofItems, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(i - 1)
            w -= itemWeights[i - 1]

    chosen_items.reverse()
    print(f"Maksymalna wartość: {dp[numberofItems][capacity]}")
    print(f"Wybrane przedmioty (indeksy): {chosen_items}")