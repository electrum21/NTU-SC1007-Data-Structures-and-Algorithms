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

    targets = {}
    for index, value in enumerate(A):
        target = K - value
        print(targets)
        if target in targets:
            dual_index[0] = targets[target]
            dual_index[1] = index
            return True
        else:
            targets[value] = index
    return False

#A and K for testing only
A = [3, 1, 7, 4, 5, 9]
K = 8

dual_index = [-1, -1]  # Initialize with invalid indices

if dual_search(A, len(A), K, dual_index):
    print(f"Pair found at indices: {dual_index}")
    print(f"Elements: {A[dual_index[0]]} + {A[dual_index[1]]} = {K}")
else:
    print("No pair found.")
