""" Implementation of Quicksort algorithm"""
#takes last element as a pivot point
def parting(arr,l,r): #l = left; r = right // smaller and greater
    i = (l-1)
    p = arr[r] # <- pivot point

    for k in range(l,r):
        if arr[k] <= p:
            i += 1
            arr[i],arr[k]=arr[k],arr[i]

    arr[i+1],arr[r] =arr[r],arr[i+1]

    return i+1

def quick_sort(arr,l,r):
    if r > l:
        sep = parting(arr,l,r)
        quick_sort(arr,l,sep-1)
        quick_sort(arr,l+1,r)


arr = [2,4,6,1,2,69,123,542,123,8,0,988,13]

quick_sort(arr,0,len(arr)-1)

print arr

# outputs [0, 1, 2, 2, 4, 6, 8, 13, 69, 123, 123, 542, 988]