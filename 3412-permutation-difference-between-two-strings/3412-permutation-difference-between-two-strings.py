class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum = 0
        for i in s:
            sum += abs(s.index(i) - t.index(i))
        return sum