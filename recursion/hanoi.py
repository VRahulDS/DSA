def toh(n, s='source', d='destination', h='helper'):
	if n == 0:
		return
		
	toh(n-1, s, h, d)
	print(s, "->", d)
	toh(n-1, h, d, s)
	
	
print(toh(3))
	
	
