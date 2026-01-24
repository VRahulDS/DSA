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
	
def merge_sort(arr):
	if len(arr)==1:
		return arr
	
	l = 0
	h = len(arr)
	m = (l+h)//2
	
	arr1 = merge_sort(arr[l:m])
	arr2 = merge_sort(arr[m:h])
	
	return merge_2_sorted(arr1, arr2)
	
	
print(merge_sort([1, 4, 2, 3, 5, 8, 7]))
		