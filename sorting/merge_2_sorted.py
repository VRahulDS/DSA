def merge_2_sorted(arr1, arr2):
	m = len(arr1)
	n = len(arr2)
	
	arr = []
	
	i = j = 0
	while (i < m) and (j < n):
		if arr1[i] <= arr2[j]:
			arr.append(arr1[i])
			i += 1
		else:
			arr.append(arr2[j])
			j += 1
	while i < m:
		arr.append(arr1[i])
		i+=1
		
	while j < n:
		arr.append(arr2[j])
		j+=1
		
	return arr
	
	
print(merge_2_sorted([1,4,7], [2, 3, 8]))