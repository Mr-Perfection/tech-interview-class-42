'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
'''

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

20 minutes
'''

'''
0   1   0   3   12
^ = i
^ = zPos

0   1   0   3   12
    ^
    ^
0   1   0   3   12
        ^
    ^
0   0   1   3   12
            ^
        ^
swap, zPos + 1

0   0   1   3   12
                ^
        ^
Time: O(n)
Space: O(1)
'''

def move_zeros(arr):
    zpos, n = 0, len(arr)

    for i in range(len(arr)):
        x = arr[i]

        if x == 0:
            # swap
            arr[i], arr[zpos] = arr[zpos], arr[i]
            zpos += 1
    print(arr)

move_zeros([1,0,0,0,4,3,2,6])
move_zeros([1,0,0,0,4,3,2,0])
move_zeros([1,0,10,0,4,3,2,0])