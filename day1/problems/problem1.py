'''
Given a nested list of integers, return the sum of all integers in the list 
weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be 
integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and 
one 6 at depth 3; 1 + 4*2 + 6*3 = 27)

[] depth = 1
[[1,1]] depth = 2
[0,[1,[2,2]]] 2 is at depth = 3, 1 is at depth = 2, o

[0,[1,[2,2]]]
=> 0 * 1 + 1 * 2 + 2 * 3 + 2 * 3 = 14. 

0 isinstanceof(list)
=> False
[1,[2,2]] isinstanceof(list)
=> True
Linkedin
'''