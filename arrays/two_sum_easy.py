# Concepts used:
# Two Pointers Technique

# Problem statement(SIMPLIFIED):
# Given an array A with N elements arranged in an ascending order, also given a number K. 
# Check if their exist two indices such that sum of elements at those indices is equal to K. 
# If Yes print those indices accordingly else print no answer.

def two_sum(arr, k):
    i = 0
    j = len(arr)-1

    while i < j:
        sum_ = arr[i] + arr[j]
        if sum_ == k:
            return (i, j)
        elif sum_ > k:
            j -= 1
        else:
            i += 1

    return "no answer"


print(two_sum([1,3,4,6,7],10))
    


