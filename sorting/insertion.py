def insertion(arr):
	
	n = len(arr)
	for i in range(1, n):
		for j in range(i, -1, -1):
			while j >=1 and arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
	return arr
	
print(insertion([1, 4, 3, 5, 2]))
print(insertion([1, 2, 8, 4, 3, 5, 2]))
			
			