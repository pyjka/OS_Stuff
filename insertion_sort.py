def insertion(listik):
	for i in range(1,len(listik)):
		key = listik[i]
		j = i-1
		while j >=0 and listik[j] > key:
			listik[j+1]=listik[j]
			j -=1
		listik[j+1] = key

listik = [9,6,8,7,1,3,2,4,5,0]
insertion(listik)

print listik
