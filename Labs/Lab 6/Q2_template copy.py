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

    left = 0
    right = len(A) - 1

    while left <= right:
        sum = A[left] + A[right]
        if sum > K:
            right -= 1
        elif sum < K:
            left += 1
        else:
            dual_index[0] = left
            dual_index[1] = right
            return True
    return False

    

#A and K for testing only
A = [9, 1, 4, 3, 7, 5]  # Unsorted array
K = 8
dual_index = [-1, -1]  # Initialize with invalid indices

if dual_sorted_search(A, len(A), K, dual_index):
    print(f"Pair found at indices: {dual_index}")
    print(f"Elements: {A[dual_index[0]]} + {A[dual_index[1]]} = {K}")
else:
    print("No pair found.")
