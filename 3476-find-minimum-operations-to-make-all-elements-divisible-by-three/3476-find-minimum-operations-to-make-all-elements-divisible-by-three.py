class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if i % 3 == 1 or i % 3 == 2:
                res += 1
        return res
        