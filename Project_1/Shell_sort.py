def steps(n):
    l_step = [1]
    length = len(n)
    k = 0

    while True:
        step = 4 ** (k + 1) + 3 * 2 ** k + 1
        if step > length:
            break
        l_step.append(step)
        k += 1
    return l_step[::-1]


def Shell(n):
    l_steps = steps(n)
    for step in l_steps:
        for i in range(step, len(n)):
            number = n[i]
            j = i
            while j >= step and n[j - step] > number:
                n[j] = n[j - step]
                j -= step
            n[j] = number

    return n

print(Shell([63, 4, 3, 2, 1, 65, 1, 123, 17, 1234, 74]))
