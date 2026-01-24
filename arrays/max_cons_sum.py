# maximum consecutive sum

def max_sum(arr, k):
    n = len(arr)
    max_ = float('-inf')
    for i in range(n-k+1):
        sum_ = arr[i] + arr[i+1] + arr[i+2]
        if max_ <= sum_:
            max_ = sum_
    return max_

print(max_sum([1,4,6,3,8,9,2,0,3],3))
    