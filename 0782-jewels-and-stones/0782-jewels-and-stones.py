class Solution:
    def numJewelsInStones(self, J, S):
        return sum(map(J.count, S))