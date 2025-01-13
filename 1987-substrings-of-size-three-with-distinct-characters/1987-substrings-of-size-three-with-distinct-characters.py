class Solution(object):
    def countGoodSubstrings(self, s):
        l, m, r = 0, 1, 2
        res = 0
        while r < len(s):
            if s[l] != s[m] and s[m] != s[r] and s[l] != s[r]:
                res += 1
            l += 1
            m += 1
            r += 1
        return res