"""Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.
"""

""" 
Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
Edge cases:
899
999
"""
import time
def plusOne(A):
	# My naive solution
    a = ''
    B = []
    for i in A:
        A[0] = B
        a += str(i)
    a = int(a) + 1
    for j in str(a) :
        for k in j:
            B.append(int(k))
    return A[0]


print  (time.time - time.time(plusOne([9,9,999,99999,99999999,9,9,9,9,9,9,9,99,99,9,9,9,9,9,99,9,9,9,9,9,9,9,9,9,9,999999]))