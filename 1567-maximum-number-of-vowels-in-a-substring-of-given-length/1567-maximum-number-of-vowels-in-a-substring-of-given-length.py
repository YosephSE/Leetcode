class Solution(object):
    def maxVowels(self, s, k):
        vowels = 'aeiou'
        maxV = 0
        v = 0
        l = 0
        for r in range(len(s)):
            if s[r] in vowels:
                v += 1
            maxV = max(v, maxV)
            if r - l + 1 == k:
                if s[l] in vowels:
                    v -= 1
                l += 1
        return maxV

                

                
        