""" Given a read only array of n + 1 integers between 1 and n, find one number that repeats
 in linear time using less than O(n) space and traversing the stream sequentially O(1) times.
 """

def repeatedNumber(A):
    zet = set()
    for i in A:
        if i in zet:
            return i
        zet.add(i)
    return None