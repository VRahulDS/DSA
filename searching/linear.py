def linear(arr, k):
	for i in range(len(arr)):
		if arr[i]==k:
			return i
	return -1
	
print(linear([1,5,8,3,6], 3))
print(linear([1,5,8,3,6], 2))