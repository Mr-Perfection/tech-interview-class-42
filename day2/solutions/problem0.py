'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


ex)
nums = 2, 7, 11, 15
map = {
    2:  0
    7:  1
    11: 2
    15: 3
}

2, i = 0
target - 2 in map? if yes, return [map[target-2], i]
'''

def Solution(nums: list, target: int):
    
    table = dict() # or {}
    for i, num in enumerate(nums):
        table[num] = i

    for i, num in enumerate(nums):
        if target - num in table:
            return sorted([table[target-num], i ]) 
    return None

print(Solution([2,7,11,15], 9))
print(Solution([2,7,11,15], 13))
print(Solution([2,7,11,15], 22))

'''
[0, 1]
[0, 2]
[1, 3]
'''