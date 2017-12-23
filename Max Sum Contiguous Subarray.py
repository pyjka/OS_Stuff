""" Find the contiguous subarray within an array 
(containing at least one number) which has the largest sum. """

def maxSubArray(self, A):
	# Solution implementing dynamic programming
    max_yet = A[0]
    max_sofar = A[0]
    for i in range(1,len(A)):
        max_yet = max(A[i],max_yet + A[i])
        max_sofar = max(max_sofar,max_yet)
    return max_sofar