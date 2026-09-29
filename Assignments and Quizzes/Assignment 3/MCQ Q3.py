listA = [1,2,3,4,5,6,7,8,9,10]
x = 5

def process_array(listA, x, n):
    i = 0
    j = n - 1

    while i <= j:
        k = (i+j) // 2
        if x <= listA[k]:
            j = k - 1
        if listA[k] <= x:
            i = k + 1
    
    if listA[k] == x:
        return k
    else:
        return -1
    
print(process_array(listA, x, 10))
    
