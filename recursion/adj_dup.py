def remove_adj_dup(st, i=0, out=""):
	n = len(st)
	if n ==i:
		return out
		
	if len(out)==0 or out[-1]!=st[i]:
		out+=st[i]
		return remove_adj_dup(st, i+1, out)
	else:
		return remove_adj_dup(st, i+1, out)
		
		
print(remove_adj_dup("aaabbbcddda"))
	