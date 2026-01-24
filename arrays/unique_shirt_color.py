# find the number with odd number of times
# using hashmap

def ucs(array):
    dic = {}
    for i in array:
        dic[i] = dic.get(i, 0) + 1
    for k, v in dic.items():
        if v%2==0:
            continue
        else:
            return k
    
print(ucs([1,2,5,2,1,5,5,1,1]))

# using XOR

def opti_ucs(array):
    soln = 0
    for i in array:
        soln = soln^i
    return soln

print(opti_ucs([1,2,5,2,1,5,5,1,1]))