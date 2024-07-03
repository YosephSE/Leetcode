class Solution:
    def minDifference(self, nums):
        if len(nums) < 5:
            return 0
        minimum = float("inf")
        nums.sort()
        for left in range(4):
            right = len(nums) - 4 + left
            minimum = min(minimum, nums[right] - nums[left])
        return minimum
    