class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split()
        strs.reverse()
        return ' '.join(strs)
        