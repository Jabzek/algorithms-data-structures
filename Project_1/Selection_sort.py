def selection(num_l):
    for el in range(len(num_l) - 1):
        min_idx = el
        for i in range(min_idx + 1, len(num_l)):
            if num_l[min_idx] > num_l[i]:
                min_idx = i
        num_l[el], num_l[min_idx] = num_l[min_idx], num_l[el]
    return num_l