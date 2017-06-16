'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)

Linkedin
'''

'''
[[1,1],2,[1,1]]
[] , depth = 1, total = 0
[[1,1]], depth = 2 => 2 * 2 = 4, total = 4
[], depth = 1
[2], depth = 1, total = 6
[[1, 1]], depth = 2, total = 6 + 4 = 10
return total

[1,[4,[6]]]
[], depth = 1, total = 0
[1], depth  = 1, total = 1
[[4,]], depth  = 2, total = 9
[[[6]]], depth = 3, total = 9 + 18 = 27
return total

'''
def helper(arr, depth):
    total = 0
    
    for i in range(len(arr)): # from 0... length of arr -1
        if isinstance(arr[i], list):
            total += helper(arr[i], depth+1)
        else:
            total += arr[i] * depth
    
    return total
    
    
    

def solution(arr):
    if not(arr): return 0

    return helper(arr, 1)

'''
test
[[1,1],2,[1,1]]
[1,1] (1 + 1) * 2 = 4, depth = 2
2   => 4 + 2 = 6, depth = 1
[1,1] (1 + 1) * 2 = 4 => 4 + 6 = 10, depth = 2

'''
