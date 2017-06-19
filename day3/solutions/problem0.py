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
            
            if right - left == m:
                if alphas[ord(s[left])-ord('a')] >= 0:
                    count += 1
                alphas[ord(s[left])-ord('a')] += 1
                left += 1
            
        return indices