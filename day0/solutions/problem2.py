# O(n), O(n)
def solution(s):

    stack = []
    for i in range(len(s)):
        el = s[i]
        s_len = len(stack)
        if el == '(' or el == '[' or el == '{':
            stack.append(s[i])
        else:
            if el == ')':
                if s_len > 0:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False 
                else:
                    return False
            if el == ']':
                if s_len > 0:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False 
                else:
                    return False
            if el == '}':
                if s_len > 0:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False 
                else:
                    return False
    # check if stack length is empty or not in the end.                    
    return True if len(stack) == 0 else False

print(solution('[][](())'))
print(solution('[][](()'))
print(solution('[][](}}[]'))

print(solution('[(())()(){{{{}}}}{()}][](()'))
print(solution('[(())()(){{{{}}}}{()}][]()'))



'''
O(n), O(n)
if you want to do recursive... 
'(())))' => false
( ())))
(( ))))
( )))
)) // invalid, FALSE

[[][[]]]]
'''
def helper(left, right):

    # storing to the left bracket
    if right:
        if right[0] == '(' or right[0] == '{' or right[0] == '[':
            return helper(left+right[0], right[1:])
    # base cases
    # both brackets do not exist
    if not(left) and not(right):
        return True
    # left brackets do not exist and right exists or vise-versa
    if not(left) or not(right):
        return False
    
    x, y = left[-1], right[0]
    
    if x == '(' and y == ')' or\
       x == '[' and y == ']' or\
       x == '{' and y == '}':
        return helper(left[0:-1], right[1:])
    else:
        return False

def solution_recursive(s):
    i = 0
    
    while s[i] == '(' or s[i] == '[' or s[i] == '{': i += 1
    
    if i == 0:
        return False
    else:
        return helper(s[0:i], s[i:])

print('--------------')
print(solution_recursive('[][](())'))
print(solution_recursive('[][](()'))
print(solution_recursive('[][](}}[]'))

print(solution_recursive('[(())()(){{{{}}}}{()}][](()'))
print(solution_recursive('[(())()(){{{{}}}}{()}][]()'))
