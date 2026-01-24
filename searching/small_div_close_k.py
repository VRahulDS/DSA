import math
def small_div(n, k):
	
	m = math.sqrt(n)
	close = -1
	dist = float('inf')
		
	
	for i in range(1, int(m)+1):
		if n%i==0:
			if abs(i-k)<dist:
				close = i
				dist = abs(i-k)
				
			if abs(n/i - k)<dist:
				close = n/i
				dist = abs(n/i-k)
				
	return close
	
	
print(small_div(16, 5))
print(small_div(27, 15))
			