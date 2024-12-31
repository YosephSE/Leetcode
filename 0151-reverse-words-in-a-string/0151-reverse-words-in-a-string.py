class Solution:
    def reverseWords(self, s: str) -> str:
        val = s.split()
        val.reverse()
        return ' '.join(val)
        