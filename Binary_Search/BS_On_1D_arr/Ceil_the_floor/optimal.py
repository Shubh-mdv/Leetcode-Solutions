def getFloorAndCeil(a, n, x):
    # Write your code here.
    floor = -1
    ceil = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return [a[mid], a[mid]]
        elif x < a[mid]:
            ceil = a[mid]
            high = mid - 1
        else:
            floor = a[mid]
            low = mid + 1
    return [floor, ceil]
