import time
import random

# --- Algorithms ---

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# --- Timing Wrapper ---

def measure_time(sort_func, data):
    start_time = time.time()
    sort_func(data)
    return time.time() - start_time

# --- Test ---

# Using a larger dataset to see a real difference
sizes = [1000, 5000, 10000, 50000, 100000]

bubble_sort_times = []
merge_sort_times = []

for size in sizes:
    arr = [random.randint(0, 100000) for _ in range(size)]
    arr_copy = arr[:]

    bubble_time = measure_time(bubble_sort, arr)
    merge_time = measure_time(merge_sort, arr_copy)

    bubble_sort_times.append(bubble_time)
    merge_sort_times.append(merge_time)

    print(f"Size: {size}, Bubble Sort Time: {bubble_time:.5f} sec, Merge Sort Time: {merge_time:.5f} sec")