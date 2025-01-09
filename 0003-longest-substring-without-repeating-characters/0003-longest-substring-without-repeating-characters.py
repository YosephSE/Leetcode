class Solution(object):
    def lengthOfLongestSubstring(self, s):
        r = 0
        maxLen = 0
        hash_set = set()
        
        for l in range(len(s)):

            while r < len(s) and s[r] not in hash_set:
                hash_set.add(s[r])
                r += 1
            maxLen = max(maxLen, r - l)
            
            hash_set.remove(s[l])
        
        return maxLen
