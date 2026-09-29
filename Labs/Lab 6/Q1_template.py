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

    # Dictionary approach, O(n) complexity checking each number once only, but uses extra memory
    seen = {}  # Dictionary to store {value: index}
    
    for current_index, val in enumerate(A):
        partner = K - val
        
        if partner in seen:
            # We found the partner! 
            dual_index[0] = seen[partner]
            dual_index[1] = current_index
            return True
        
        # If not found, store the current number and move on
        seen[val] = current_index
        
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
