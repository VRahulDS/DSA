def lower_bound_arr(arr,  k):
	l = 0
	h = len(arr)-1
	found = False
	
	while l<=h:		
		mid = (l+h)//2
	#	print(l, h, mid)
		if arr[mid] < k:
			l = mid +1
		elif arr[mid] == k:
			h = mid - 1
			found = True
		elif arr[mid] > k:
			h = mid-1
	
	if found:		
		return l
	else:
		return  -1
		
print(lower_bound_arr([1,2,2,2,3, 3, 34,5,6], 3))
print(lower_bound_arr([1,2,3,4,6], 1))
