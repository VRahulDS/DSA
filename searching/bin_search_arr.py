def bin_search_arr(arr,  k):
	l = 0
	h = len(arr)-1
	
	while l<=h:
		mid = (l+h)//2
		
		if arr[mid] == k:
			return mid
		elif arr[mid] > k:
			h = mid-1
		else:
			l = mid +1
			
	return -1
		
print(bin_search_arr([1,2,3,4,5,6], 1))
print(bin_search_arr([1,2,3,4,6], 1))