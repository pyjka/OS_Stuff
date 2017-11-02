def insertion(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >=0 and arr[j] > key:
			arr[j + 1]=arr[j]
			j -=1
		arr[j + 1] = key

listik = [9,6,8,7,1,3,2,4,5,0]
insertion(listik)

print listik
