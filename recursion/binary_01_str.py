def binary(n, st=''):
	if n ==0:
		print(st)
		return
	if len(st)==0:
		st = '0'
		binary(n-1, st)
		st = st[:-1]
		st = '1'
		binary(n-1, st)
	elif st[-1]=='0':
		st += '0'
		binary(n-1, st)
		st = st[:-1]
		st += '1'
		binary(n-1, st)
	elif st[-1]=='1':
		st += '0'
		binary(n-1, st)
		
binary(3)