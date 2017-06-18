'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''
def wordPattern(pattern, str):
    '''
    ex)
    pattern = a b c d, str = cat dkg asdf la, True
    pattern = a b c a, str = cat dog dogs cats, False
    pattern = a b b a, str = cat dog dog cat, True
    
    map patterns with elements in lst
    
    time and space: O(n), O(n), n = length of pattern and length of lst
    '''
    lst = str.split(' ')
    ptable, stable = {}, {}
    
    if not pattern or not str or len(pattern) != len(lst):
        return False
        
    for i,c in enumerate(pattern):
        if c not in ptable:
            ptable[c] = lst[i]
        else:
            if ptable[c] != lst[i]:
                return False
        if lst[i] not in stable:
            stable[lst[i]] = c    
        else: 
            if stable[lst[i]] != c:
                return False
    return True
        
        