class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        indices = []
        n,m = len(s), len(p)
        # check if p.length < s.length
        if m > n:
            return []
        
        # alphabets array stores occurences of letters inside p
        alphas = [0 for i in range(26)]
        
        # initialize alphas with p
        for c in p:
            alphas[ord(c)-ord('a')] += 1
        
        # sliding window algorithm O(n)
        right,left, count = 0, 0, m
        while right < n:
            
            # check if char from s exists in alphas
            if alphas[ord(s[right])-ord('a')] >= 1:
                count -= 1
            
            # decrements the alpha value
            alphas[ord(s[right])-ord('a')] -= 1
            # move right every time
            right += 1


            if count == 0:
                indices.append(left)
            
            # if s[left:right].length == p.length
            # then we need to fix left location
            if right - left == m:
                # check whether leftmost element
                left_char_val = ord(s[left])-ord('a')
                # increment count because this letter has been decremented previously
                if alphas[left_char_val] >= 0:
                    count += 1
                alphas[left_char_val] += 1
                left += 1

        return indices

'''
s = abcdecbabc
p = cab

alphas = [1,1,1,0....]
right = 0
left=0, right=0, count=3, alphas = [1,1,1,0....]
left=0, right=0, count=2, alphas = [0,1,1,0....]
left=0, right=1, count=2, alphas = [0,1,1,0....]
left=0, right=2, count=1, alphas = [0,0,1,0....]
left=0, right=3, count=0, alphas = [0,0,0,0....] -> [0]


'''