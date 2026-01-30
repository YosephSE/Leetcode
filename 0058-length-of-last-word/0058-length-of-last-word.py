class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.strip().split()[-1]
        return len(new_s)
        