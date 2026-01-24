def fact(n):
	if (n==1) or (n==0):
		return 1
		
	prev = fact(n-1)
	return n*prev
	
	
print(fact(5))