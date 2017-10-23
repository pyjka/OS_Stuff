def sorting(listik):
    n = (listik)
    for i in range(len(n)):
        smallest = i
        for j in range(i+1,len(n)):
            if n[smallest] > n[j]:
                smallest = j
            n[i], n[smallest] = n[smallest], n[i]


listik1 = [123,81,35,4,17,21,76,29,110,313]
sorting(listik1)

print listik1

