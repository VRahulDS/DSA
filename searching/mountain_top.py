def mountain_top(arr, l=-1, h=-1):
	if l==-1:
		l = 0
		h = len(arr)-1
	n = len(arr)
	
	mid = (l+h)//2
	
	if len(arr) == 1:
		return 0
	
	elif (mid==0) and (mid+1==h-1):
		if arr[mid] > arr[mid+1]:
			return mid
		else:
			return mid+1
			
	if arr[mid] < arr[mid-1] :
		return mountain_top(arr, l, mid-1)
		
	elif arr[mid] < arr[mid + 1]:
		return mountain_top(arr, mid+1, h)
		
	else:
		return mid
	
print(mountain_top([1,2,3,7,5,4,3]))
	