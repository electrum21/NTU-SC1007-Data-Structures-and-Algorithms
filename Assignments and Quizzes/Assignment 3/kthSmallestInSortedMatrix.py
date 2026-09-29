def kth_smallest(matrix, k):

    # Below block of code doesnt pass for 1 test case, because same number may appear in different rows
    # no_of_elements_per_sublist = len(matrix[0])
    # if k <= no_of_elements_per_sublist:
    #     return matrix[0][k-1]
    # else:
    #     row_to_access = (k-1) // no_of_elements_per_sublist
    #     col_to_access = (k-1) % no_of_elements_per_sublist
    #     return matrix[row_to_access][col_to_access]

    flat_list = [element for row in matrix for element in row]
    flat_list.sort()
    return flat_list[k-1]

#read the input
n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
#output
print(kth_smallest(matrix, k))