def bin_search_arr(arr,  k, l, h):
	if l>h:
		return -1
	mid = (l+h)//2
	
	if arr[mid]==k:
		return mid
	elif arr[mid] > k:
		return bin_search_arr(arr, k, 0, mid-1)
	else:
		return bin_search_arr(arr, k, mid+1, h)
		
		
print(bin_search_arr([1,2,3,4,5,6], 2, 0, 5))
print(bin_search_arr([1,2,3,4,6], 1, 0, 4))