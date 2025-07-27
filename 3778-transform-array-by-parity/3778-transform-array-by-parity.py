class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if i % 2 == 0:
                res.append(0)
            else: 
                res.append(1)

        return sorted(res)

        