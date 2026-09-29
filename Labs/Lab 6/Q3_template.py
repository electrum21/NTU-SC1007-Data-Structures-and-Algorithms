def dual_search(A, size, K, dual_index):
    """
    Finds two elements in the array whose sum is equal to K.

    Parameters:
    A (list): The input array of integers.
    size (int): The size of the array.
    K (int): The target sum.
    dual_index (list): A list to store the indices of the two elements.

    Returns:
    bool: True if a pair is found, False otherwise.
    """

    # Nested loops, O(n^2) complexity checking every possible pair
    for i in range(size):
        for j in range(i, size):
            if A[i] + A[j] == K:
                # Note: due to Python scoping, need to strictly modify the dual_index list contents instead of dual_index = [i,j]
                dual_index[0] = i
                dual_index[1] = j
                return True
    
    return False

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


def dual_sorted_search(A, size, K, dual_index):
    """
    Finds two elements in the sorted array whose sum is equal to K.

    Parameters:
    A (list): The input array (will be sorted first).
    size (int): The size of the array.
    K (int): The target sum.
    dual_index (list): A list to store the indices of the two elements.

    Returns:
    bool: True if a pair is found, False otherwise.
    """
    merge_sort(A)  # Sort the array first

    i = 0
    j = size - 1

    while i <= j:
        if A[i] + A[j] == K:
            dual_index[0] = i
            dual_index[1] = j
            return True
        elif A[i] + A[j] < K:
            i += 1
        else:
            j -=1
    
    return False


def read_file(filename):
    """
    Reads a file where the first line is the search key, the second line is the data size, and the rest are the data.

    Parameters:
    filename (str): The file path to read data from.

    Returns:
    tuple: (search_key, data) where search_key is an integer and data is a list of integers.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    search_key = int(lines[0].strip())
    data_size = int(lines[1].strip())  # Ensure correctness but not used directly
    data = list(map(int, lines[2:]))

    return search_key, data


# To read files
file_500k = "input_500k.txt"
file_1m = "input_1mil.txt"

search_key_500k, data_500k = read_file(file_500k)
search_key_1m, data_1m = read_file(file_1m)
dual_index_1 = [-1, -1]
dual_index_2 = [-1, -1]

if dual_sorted_search(data_500k, len(data_500k), search_key_500k, dual_index_2):
    print(f"Pair found at indices: {dual_index_2}")
    print(f"Elements: {data_500k[dual_index_2[0]]} + {data_500k[dual_index_2[1]]} = {search_key_500k}")
else:
    print("No pair found.")

if dual_sorted_search(data_1m, len(data_1m), search_key_1m, dual_index_1):
    print(f"Pair found at indices: {dual_index_1}")
    print(f"Elements: {data_1m[dual_index_1[0]]} + {data_1m[dual_index_1[1]]} = {search_key_1m}")
else:
    print("No pair found.")

if dual_search(data_500k, len(data_500k), search_key_500k, dual_index_2):
    print(f"Pair found at indices: {dual_index_2}")
    print(f"Elements: {data_500k[dual_index_2[0]]} + {data_500k[dual_index_2[1]]} = {search_key_500k}")
else:
    print("No pair found.")

if dual_search(data_1m, len(data_1m), search_key_1m, dual_index_1):
    print(f"Pair found at indices: {dual_index_1}")
    print(f"Elements: {data_1m[dual_index_1[0]]} + {data_1m[dual_index_1[1]]} = {search_key_1m}")
else:
    print("No pair found.")
