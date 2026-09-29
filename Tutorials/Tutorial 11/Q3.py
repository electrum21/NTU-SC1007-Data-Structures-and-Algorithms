def find_minimum(array, m, n):
    if m == n:
        return array[m]
    else:
        middle = (m+n) // 2
        if array[middle] < array[n]: # in the first half
            return find_minimum(array, m, middle) 
        else: # in the second half
            return find_minimum(array, middle+1, n)
    
array = [3, 4, 5, 6, 7, 8, 1, 2]
minimum = find_minimum(array, 0, len(array) - 1)
print(f"the minimum value is {minimum}")

# Run time: T(n) = T((n/2)) + c

