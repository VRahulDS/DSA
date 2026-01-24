def num_comb(arr, k, i=0, out=[]):
	if k == i:
		print(out)
		return
	
	for num in range(len(arr)):
		out[i] = arr[num]
		num_comb(arr[num+1:], k, i+1, out)
		
print(num_comb([1,2,3,4,5], 2, 0, [-1, -1]))
	
	
	
