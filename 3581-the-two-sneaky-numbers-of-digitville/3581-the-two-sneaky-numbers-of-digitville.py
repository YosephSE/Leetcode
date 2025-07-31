class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        unique_nums = {}
        for i in nums:
            if i in unique_nums:
                res.append(i)
            else:
                unique_nums[i] = True
        return res
        