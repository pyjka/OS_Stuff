""" implementation of a merge sort algorithm """

def merge_sort(arr):
    if len(arr) == 0 or 1:
        return None
    q = (len(arr)/ 2)

