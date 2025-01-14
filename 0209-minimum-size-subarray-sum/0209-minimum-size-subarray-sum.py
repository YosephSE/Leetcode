class Solution(object):
    def minSubArrayLen(self, target, nums):
        l, r = 0, 0
        pre_sum = 0
        min_len = float('inf')
        
        while r < len(nums):
            pre_sum += nums[r]
            while pre_sum >= target:
                min_len = min(min_len, r - l + 1)
                pre_sum -= nums[l]
                l += 1
            r += 1
        
        return 0 if min_len == float('inf') else min_len
