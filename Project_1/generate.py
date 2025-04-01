#Remember to pip3 install numpy
import numpy as np

def generate_random_array(size):
    return np.random.randint(0, 10000, size, dtype=int)

def generate_increasing_array(size):
    return np.arange(size)

def generate_decreasing_array(size):
    return np.arange(size, 0, -1)

def generate_constant_array(size, value=42):
    return np.full(size, value)

def generate_a_shaped_array(size):
    half_size = size // 2
    increasing_part = np.arange(half_size)
    decreasing_part = np.arange(half_size, 0, -1)
    return np.concatenate((increasing_part, decreasing_part))

def generate_all_arrays(sizes):
    arrays = {}
    idx = 0
    for size in sizes:
        arrays[idx] = {
            "random": generate_random_array(size),
            "increasing": generate_increasing_array(size),
            "decreasing": generate_decreasing_array(size),
            "constant": generate_constant_array(size),
            "a_shaped": generate_a_shaped_array(size)
        }
        idx += 1
    return arrays

sizes = [2**x for x in range(2, 17)]


