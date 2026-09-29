def find_minimum(array, m, n):
    if m == n:
        return array[m]
    else:
        middle = (n + m) // 2

        if array[middle] < array[n]:  # in the first half
            return find_minimum(array, m, middle)
        else:  # in the second half
            return find_minimum(array, middle + 1, n)

        