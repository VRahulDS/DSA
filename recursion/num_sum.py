def numsum(n):
	if n==1:
		return 1
	return numsum(n-1)+n
	
	
	
print(numsum(5))