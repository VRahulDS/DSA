# Given N ages of students of a college and some conditions which determine whether A can Friend Request B or not. 
# Determine the total no. of Friend Requests that can be made.
# Conditions:
# age[B] <= 0.5* age[A] + 7
# age[B] > 100 && age[A] <100
# age[B] > age[A]


def friends(nums):
    soln = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j:
                if (nums[j] <= 0.5*nums[i]+7) or ((nums[j]>100) and (nums[i]<100)) or (nums[j] > nums[i]):
                    soln +=1

    return soln

print(friends([17,18,19]))


def opti_friends(nums):
    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1

    soln = 0
    for k1, v1 in dic.items():
        for k2, v2 in dic.items():
            if (k2 <= 0.5*k1+7) or ((k2>100) and (k1<100)) or (k2 > k1):
                if k1 == k2:
                    soln += v1 * (v2 - 1)
                else:
                    soln += v1 * v2
    return soln


print(opti_friends([17,18,19]))

