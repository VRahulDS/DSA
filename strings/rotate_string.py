#rotate string (fake password)

def rotate_str(s, goal):
	n1 = len(s)
	n2 = len(goal)
	
	if n1!=n2:
		return False
		
	ind = []
	for i in range(n1):
		if s[i] == goal[0]:
			ind.append(i)
			
	for i in ind:
		
		if s[i:]+s[:i] == goal:
			return True
	return False
		
		
print(rotate_str("rahul", "uhlra"))
print(rotate_str("rahul", "hulra"))
print(rotate_str("rahaul", "aulrah"))


		
	
	