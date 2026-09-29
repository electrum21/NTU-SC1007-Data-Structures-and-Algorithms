import time #to be used to measure execution time
import matplotlib.pyplot as plt # to be used to plot execution times

def recursive_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def iterative_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for _ in range(3, n + 1):
        c = a+b
        b = a
        a = c
    return c

def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    exec_time = time.time() - start_time
    return exec_time, result

n_values = [20, 30, 40, 45]
recursive_times = []
iterative_times = []
recursive_results = []
iterative_results = []

for n in n_values:
    rec_time, rec_result = measure_time(recursive_fibonacci, n)
    itr_time, itr_result = measure_time(iterative_fibonacci, n)

    recursive_times.append(rec_time)
    iterative_times.append(itr_time)
    recursive_results.append(rec_result)
    iterative_results.append(itr_result)

    print(f"n: {n}, Recursive Fibonacci: {rec_result}, Recursive Time: {rec_time:.5f} sec\n")
    print(f"n: {n}, Iterative Fibonacci: {itr_result}, Iterative Time: {itr_time:.5f} sec\n")