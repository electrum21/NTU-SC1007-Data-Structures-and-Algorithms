def find_lcs(n, A, B):
    """
    Parameters:
    n (int): The number of elements in sequences A and B.
    A (list): A permutation of integers from 1 to n.
    B (list): A permutation of integers from 1 to n.
    
    Returns:
    tuple: (max_length, total_count)
    """

    # initial approach of building n x n table, but has memory issue

    # # length: LCS length for A[:i] and B[:j]
    # # count: no. of unique LCS of the lengths
    # length = [[0] * (n+1) for _ in range(n+1)]
    # count  = [[0] * (n+1) for _ in range(n+1)]

    # # base case: make empty subsequences have count of 1
    # for i in range (n+1):
    #     count[i][0] = 1
    # for j in range(n+1):
    #     count[0][j] = 1

    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         if A[i-1] == B[j-1]:
    #             # if the characters match, then extend the LCS from the diagonal
    #             length[i][j] = length[i-1][j-1] + 1   
    #             count[i][j] = count[i-1][j-1]
    #         else:
    #             left = length[i][j-1]
    #             top = length[i-1][j]

    #             if top > left:
    #                 length[i][j] = top
    #                 count[i][j] = count[i-1][j]
    #             elif left > top:
    #                 length[i][j] = left
    #                 count[i][j] = count[i][j-1]
    #             else:
    #                 length[i][j] = top
    #                 count[i][j] = count[i-1][j] + count[i][j-1]
    #                 # subtract the diagonal if it represents the same length
    #                 # otherwise it's a shorter LCS and was not double counted
    #                 if length[i-1][j-1] == top:
    #                     count[i][j] -= count[i-1][j-1]
    
    # return length[n][n], count[n][n]

    pos = {x: i + 1 for i, x in enumerate(B)}  # 1-based positions
    seq = [pos[x] for x in A]

    class Fenwick:
        def __init__(self, n):
            self.n = n
            self.bit = [(0, 0)] * (n + 2)  # (best_len, count)

        def merge(self, a, b):
            if a[0] > b[0]:
                return a
            if b[0] > a[0]:
                return b
            if a[0] == 0:
                return (0, 0)
            return (a[0], a[1] + b[1])

        def update(self, i, val):
            while i <= self.n:
                self.bit[i] = self.merge(self.bit[i], val)
                i += i & -i

        def query(self, i):
            res = (0, 0)
            while i > 0:
                res = self.merge(res, self.bit[i])
                i -= i & -i
            return res

    fw = Fenwick(n)

    for x in seq:
        best_len, ways = fw.query(x - 1)
        if best_len == 0:
            cur = (1, 1)
        else:
            cur = (best_len + 1, ways)
        fw.update(x, cur)

    ans_len, ans_cnt = fw.query(n)
    return ans_len, ans_cnt


line1 = input().split()
if line1:
    n = int(line1[0])
    
    # Read array A
    A = list(map(int, input().split()))
    
    # Read array B
    B = list(map(int, input().split()))
    
    max_length, total_count = find_lcs(n, A, B)
        
    # Output in the required format
    print(f"Max Length: {max_length}")
    print(f"Total Count: {total_count}")
