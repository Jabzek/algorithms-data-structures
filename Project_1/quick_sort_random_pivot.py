import random

def quick_sort_random_pivot(arr, l, r):
    if l < r:
        q=partition(arr, l, r)
        quick_sort_random_pivot(arr, l, q)
        quick_sort_random_pivot(arr, q+1, r)

    return arr


def partition(arr, l, r):
    pivot_index = random.randint(l, r)
    x = arr[pivot_index]
    i = l
    j = r
    while True:
        while arr[j] > x: j-=1
        while arr[i] < x: i+=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
        else: return j    