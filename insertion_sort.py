def insertion(listik):
	for i in range(1,len(listik)):
		key = listik[i]
		j = i-1
		while j >=0 and listik[j] > key:
			listik[j+1]=listik[j]
			j -=1
		listik[j+1] = key
		
listik = [1,93,3,4,9,5,10,12,11,13,109,913]
insertion(listik)

print listik
