""" implementation of a merge sort algorithm """
def merge(arr,l,m,r):
    first = m - l +1
    last = r - m
    L = [0] * (first)
    R = [0] * (last)

    for i in range(0,first):
        L[i] = arr[l + i]

    for j in range(0,last):
        R[j] = arr[m + 1 + j]

    i,j,k = 0,0,l

    while i  < first and j < last:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < first:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < last:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr,l,r):
    if l <r:
        mid = (l+(r-1))/2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        merge(arr,l,mid,r)


arr = [1, 6, 3, 2, 8, 9, 7, 11, 22, 8, 12, 0, 4, 13, 5]

merge_sort(arr, 0, len(arr) - 1)

print arr

#output [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 11, 12, 13, 22]