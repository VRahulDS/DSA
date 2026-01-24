def selection(arr):
	n = len(arr)
	for i in range(n-1):
		min_ = arr[i]
		min_ind = i
		for j in range(i+1, n):
			if arr[j] < min_:
				min_ind = j
				min_ = arr[j]
				
		arr[i], arr[min_ind] = arr[min_ind], arr[i]
		
	return arr
	
	
print(selection([1, 5, 4, 3, 8]))