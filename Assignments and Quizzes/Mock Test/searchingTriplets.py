# import sys
# input = sys.stdin.read
# data = input().split()

    # Iterate through each element as the potential middle element (y)
    # Optimized Approach [O(N^2)]
    # Since the equation A[y] - A[x] = A[z] - A[y] is equivalent to 2 A[y] = A[x] + A[z], 
    # for every element A[y] acting as the middle element, you need to find how many pairs (A[x], A[z]) 
    # satisfy A[x] + A[z] = 2 A[y].

def solve(N, A):
    count = 0
    # Iterate through each element as the potential middle element (y)
    for y in range(1, N - 1):
        x = y - 1
        z = y + 1
        
        # Two-pointer approach
        while x >= 0 and z < N:
            target = 2 * A[y]
            current_sum = A[x] + A[z]
            
            if current_sum == target:
                count += 1
                x -= 1
                z += 1
            elif current_sum < target:
                z += 1
            else:
                x -= 1
    return count
        
# N = int(data[0])
# A = list(map(int, data[1:]))
# print(solve(N,A))

def run_tests():
    passed = 0
    failed = 0
 
    def test(description, A, expected):
        nonlocal passed, failed
        result = solve(len(A), A)
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        print(f"[{status}] {description}: got {result}, expected {expected}")
 
    # Classic arithmetic progression: every consecutive triple qualifies
    test("Consecutive integers [1,2,3,4,5]",
         [1, 2, 3, 4, 5], 4)
 
    # All same elements: every triple (x, y, z) with x<y<z qualifies
    # For [2,2,2,2]: y can be index 1 or 2
    #   y=1: x=0,z=2 → 2+2=4=2*2 ✓; then x=-1 stop → 1 triplet
    #   y=2: x=1,z=3 → 2+2=4=2*2 ✓; then x=0,z=4 stop → 1 more triplet
    test("All equal elements [2,2,2,2]",
         [2, 2, 2, 2], 2)
 
    # No arithmetic triplets
    test("No arithmetic triplets [1,2,4,8]",
         [1, 2, 4, 8], 0)
 
    # Minimum size array (N=3), one valid triplet
    test("Minimum array, one valid triplet [1,2,3]",
         [1, 2, 3], 1)
 
    # Minimum size array, no valid triplet
    test("Minimum array, no valid triplet [1,2,4]",
         [1, 2, 4], 0)
 
    # Negative numbers
    test("Includes negatives [-3, 0, 3]",
         [-3, 0, 3], 1)
 
    # Mixed negatives and positives
    test("Mixed [-1, 0, 1, 2, 3]",
         [-1, 0, 1, 2, 3], 4)
 
    # Large uniform gap
    test("Large uniform gap [0, 5, 10, 15]",
         [0, 5, 10, 15], 2)
 
    # Single triplet buried in non-AP array
    test("One valid triplet among noise [1, 3, 5, 8, 12]",
         [1, 3, 5, 8, 12], 1)
 
    print(f"\nResults: {passed} passed, {failed} failed")
 
run_tests()