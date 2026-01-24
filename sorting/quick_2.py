def partition(arr,l,h):
	pivot = arr[h]
	i = l
	j = h-1
	while i<=j:
		while i<h and arr[i] <= pivot:
			i+=1
		while j>=l and arr[j]>pivot:
			j-=1
		if i<=j:
			arr[i],arr[j]=arr[j],arr[i]
			
	arr[h], arr[i] = arr[i], arr[h]
	return i
	
def quick(arr,l,h):
	if h>l:
		p = partition(arr,l,h)
		quick(arr, l, p-1)
		quick(arr, p+1, h)
		
	return arr
	
print(quick([1,4,3,5], 0, 3))
print(quick([1,4,3,5, 0], 0, 4))
		