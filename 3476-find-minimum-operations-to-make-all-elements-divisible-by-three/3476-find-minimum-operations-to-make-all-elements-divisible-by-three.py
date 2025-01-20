class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if i % 3 != 0:
                res += 1
        return res
        