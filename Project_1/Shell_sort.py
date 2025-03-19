def steps(num_l):
    l_step = [1]
    length = len(num_l)
    k = 0

    while True:
        step = 4 ** (k + 1) + 3 * 2 ** k + 1
        if step > length:
            break
        l_step.append(step)
        k += 1
    return l_step[::-1]


def shell_sort(num_l):
    l_steps = steps(num_l)
    for step in l_steps:
        for i in range(step, len(num_l)):
            number = num_l[i]
            j = i
            while j >= step and num_l[j - step] > number:
                num_l[j] = num_l[j - step]
                j -= step
            num_l[j] = number

    return num_l
