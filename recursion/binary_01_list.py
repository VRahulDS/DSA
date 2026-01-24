def bin_list(n, out, prev=0,i=0):
	if n==i:
		print(out)
		return
	if prev == 0:
		out[i] = 0
		bin_list(n, out, 0, i+1)
		out[i] = 1
		bin_list(n, out, 1, i+1)
	else:
		out[i] = 0
		bin_list(n, out, 0, i+1)
		
bin_list(5, [-1]*5)