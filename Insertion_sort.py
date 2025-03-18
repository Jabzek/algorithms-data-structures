def insertion(num_l):
    for el in range(1, len(num_l)):
        number = num_l[el]
        idx = el - 1
        
        while idx >= 0 and num_l[idx] > number:
            num_l[idx + 1] = num_l[idx]
            idx -= 1
        num_l[idx + 1] = number
    return num_l