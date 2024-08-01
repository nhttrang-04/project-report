def binary_search_helper(x, A, i, j):
    '''
    Searches A for an element x using binary search. Returns the index of x if
    x is in A, or -1 if x is not in A.

    i is a lower bound on the index of x in A, and j is an upper bound on the
    index of x in A.

    Find all the indices
    '''
    indices = []
    while i < j:
        mid = i + (j - i) // 2
        if A[mid] == x:
            indices.append(mid)
            # Check left side
            left = mid - 1
            while left >= i and A[left] == x:
                indices.append(left)
                left -= 1
            # Check right side
            right = mid + 1
            while right < j and A[right] == x:
                indices.append(right)
                right += 1
            return indices
        elif A[mid] < x:
            i = mid + 1
        else:
            j = mid
    return indices

def binary_search(x, A):
    '''
    A curried version of `binary_search_helper` that searches all of A.
    '''
    return binary_search_helper(x, A, 0, len(A))
'''Example use'''
sorted_array = [3, 15, 7, 7, 12, 19, 3, 10, 1, 15]
target = 7
'''find all indices'''
result_indices = binary_search(target, sorted_array)
'''print the result'''
if result_indices:
    print(f"The target element {target} was found at indices: {result_indices}")
else:
    print(f"The target element {target} was not found in the array.")