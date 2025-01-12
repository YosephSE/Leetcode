class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages= []
        while len(nums) > 0:
            averages.append((nums[0] + nums[-1]) / 2)
            nums.pop(0)
            nums.pop(-1)
        return min(averages)
        