def binary_search(lst, key):
    lst.sort() # Binary search starts with a sorted list
    left = 0 # The first value of the list
    right = len(lst) - 1 # The last value of the list
    
    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == key:
            print("Middle element")
            return middle
        elif lst[middle] > key:
            print("Checking right side")
            right = middle - 1
        else:
            print("Checking left side")
            left = middle + 1
    return -1