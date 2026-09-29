def longest_subarray(arr, K):

    # Sliding window approach: save all zero indices into a list
    list_of_zero_indices = [-1]
    for i in range(len(arr)):
        if arr[i] == 0:
            list_of_zero_indices.append(i)
    list_of_zero_indices.append(len(arr))

    # No. of 0s (k) is controlled by the list_of_zero_indices[i + K + 1] - list_of_zero_indices[i] - 1
    # The last -1 is due to the start of the list having index -1 and end of the list having len(arr)
    max_length = 0

    # try:
    #     for i in range(len(list_of_zero_indices)):
    #         if list_of_zero_indices[i + K + 1] - list_of_zero_indices[i] - 1 > max_length:
    #             max_length = list_of_zero_indices[i + K + 1] - list_of_zero_indices[i]  - 1
    # except:
    #     pass

    # Alternatively instead of using try-except, handle the limit explicitly
    limit = len(list_of_zero_indices) - (K + 1)
    for i in range(limit):
        current_length = list_of_zero_indices[i + K + 1] - list_of_zero_indices[i] - 1
        if current_length > max_length:
            max_length = current_length
    
    return max_length


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
def run_tests():
    passed = 0
    failed = 0
 
    def test(description, arr, K, expected):
        nonlocal passed, failed
        result = longest_subarray(arr, K)
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        print(f"[{status}] {description}: got {result}, expected {expected}")
 
    # Basic case: K=1 zero allowed
    test("K=1, one zero in middle",
         [1, 1, 0, 1, 1], 1, 5)
 
    # K=0: no zeros allowed, longest run of non-zeros
    test("K=0, no zeros allowed",
         [1, 0, 1, 1, 0, 1], 0, 2)
 
    # K equals total number of zeros → entire array
    test("K equals number of zeros, entire array is answer",
         [1, 0, 1, 0, 1], 2, 5)
 
    # All zeros, K=0 → length 0
    test("All zeros, K=0 yields 0",
         [0, 0, 0], 0, 0)
 
    # All zeros, K equals length → entire array
    test("All zeros, K equals array length",
         [0, 0, 0], 3, 3)
 
    # No zeros in array
    test("No zeros in array, any K gives full length",
         [1, 1, 1, 1], 2, 4)
 
    # K larger than zeros present → entire array
    test("K larger than number of zeros in array",
         [1, 0, 1], 5, 3)
 
    # Zeros bunched at start
    test("Zeros at start, K=1",
         [0, 0, 1, 1, 1], 1, 4)
 
    # Zeros bunched at end
    test("Zeros at end, K=1",
         [1, 1, 1, 0, 0], 1, 4)
 
    # Longer array with spread zeros
    test("Spread zeros, K=2",
         [1, 0, 1, 1, 0, 1, 1, 1, 0, 1], 2, 8)
 
    # Single element array, no zeros
    test("Single non-zero element, K=0",
         [1], 0, 1)
 
    # Single element array, zero, K=1
    test("Single zero element, K=1",
         [0], 1, 1)
 
    print(f"\nResults: {passed} passed, {failed} failed")
 
run_tests()
 