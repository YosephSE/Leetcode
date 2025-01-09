class Solution(object):
    def waysToSplitArray(self, nums):
        prefix = []
        total = 0
        splits = 0
        for i in nums:
            total += i
            prefix.append(total)
        total = 0
        for i in range(len(nums) - 1, 0 ,-1):
            total += nums[i]
            if prefix[i - 1] >= total:
                splits += 1


        return splits