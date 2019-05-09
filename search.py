#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    try:
        if array[index] == item:
            return index
        else: 
            return linear_search_recursive(array, item, index+1)
    except IndexError:
        return None


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if item == array[middle]:
            return middle
        elif array[middle] < item:
            left = middle + 1
        else:
            right = middle - 1

    return None
    

def binary_search_recursive(array, item, left=None, right=None):
    
    if left is None and right is None:
        print("Searching for", item, " in ", array)
        left = 0
        right = len(array) - 1

    window = right + left
    middle =  window // 2
    # print(middle)
    if array[middle] == item:
        return middle
    elif array[middle] < item:
        left = middle + 1
    else:
        right = middle - 1
    if not right < left:
        return binary_search_recursive(array, item, left, right)
    else:
        return None
