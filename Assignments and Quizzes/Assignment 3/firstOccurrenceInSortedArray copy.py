def first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            high = mid - 1
            result = mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return result
    
n, target = map(int, input().split())
arr = list(map(int, input().split()))
result = first_occurrence(arr, target)
print(result)