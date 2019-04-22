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
    # TODO: implement binary search iteratively here
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
    # TODO: implement binary search iteratively here
    


def binary_search_recursive(array, item, left=None, right=None):
    print("Searching for", item, " in ", array)
    middle = len(array) // 2
    if array[middle] == item:
        return middle
    elif array[middle] < item:
        new_slice = array[middle:]
    else:
        new_slice = array[:middle]  
    print(item, array, new_slice)  
    if len(new_slice) > 1:
        return binary_search_recursive(new_slice, item)
    else:
        return None

    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
