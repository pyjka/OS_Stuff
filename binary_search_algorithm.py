def binarysearch(listik,x):
    p = 1
    r = len(listik)
    while p <= r:
        q = (p+r)//2
        if listik[q] == x:
            return q
        elif listik[q]> x:
            return r == (q - 1)
        else:
            if listik[q] < x:
                return p ==(q + 1)
    return None

listik = [1,2,3,4,5,6,7,8,9,10]

print binarysearch(listik,6)

