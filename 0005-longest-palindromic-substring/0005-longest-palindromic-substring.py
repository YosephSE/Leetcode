class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            r, l = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(res) <  (r - l + 1):
                    res = s[l: r + 1]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(res) <  (r - l + 1):
                    res = s[l: r + 1]
                l -= 1
                r += 1
        return res

        