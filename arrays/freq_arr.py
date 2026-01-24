def freq(array):
    dic = {}
    for i in array:
        dic[i] = dic.get(i, 0) + 1
    return dic

print(freq([1,2,3,5,2,4,2,4,2,3,1]))