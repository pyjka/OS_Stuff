def search(A,B):
        q = 0
    	for i in range(len(A)-1):
		if A[i] > A[i+1]:
			q = i
    	for i in range(len(A[:q])):
    		if B == A[i]:
    			return i
    	for i in A[q:]:
    		if B in A[q:]:
    			return A.index(B)
    	return -1


print search([213123,212313213,2345412313,983,678,9134], 983) #outputs 3	