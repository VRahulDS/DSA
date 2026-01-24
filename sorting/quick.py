def partition(arr, l, h):
	pivot = arr[l]
	i =l+1
	j=h
	
	while i<=j:
		while i <= h and arr[i] <= pivot:
			i +=1
		while (arr[j] > pivot):
			j -=1
		if i<j:
			arr[i],arr[j] = arr[j],arr[i]
		else:
			break
	arr[l], arr[j] = arr[j], arr[l]
	return j
	
def quick(arr,l,h):
	if (l<h):
		p = partition(arr,l,h)
		quick(arr,l,p-1)
		quick(arr,p+1,h)
	return arr
	
print(quick([1,4,5,3,8,2],0,5))