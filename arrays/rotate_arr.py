def reverse(arr, i, j):
	while i <= j:
		arr[i], arr[j] = arr[j], arr[i]
		i+=1
		j-=1
	
	
def rotate(arr, k):
	n = len(arr)
	k = k%n
	reverse(arr, 0, k-1)
	reverse(arr, k, n-1)
	reverse(arr, 0, n-1)
	return arr


#print(reverse([1,2,3,4,5], 1, 3))
print(rotate([1,2,3,4,5], 2))
print(rotate([1,2,3,4,5,6,7,8], 3))