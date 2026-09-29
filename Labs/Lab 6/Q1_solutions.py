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
    for i in range(size):
        for j in range(size):
            if A[i] + A[j] == K:  # The two elements can be the same
                dual_index[0] = i
                dual_index[1] = j
                return True  # Pair found, terminate the function

    return False  # No pair found

A = [3, 1, 7, 4, 5, 9]
K = 8
dual_index = [-1, -1]  # Initialize with invalid indices

if dual_search(A, len(A), K, dual_index):
    print(f"Pair found at indices: {dual_index}")
    print(f"Elements: {A[dual_index[0]]} + {A[dual_index[1]]} = {K}")
else:
    print("No pair found.")
