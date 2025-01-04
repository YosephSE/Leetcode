class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return sorted(set(nums))[-1]
        return sorted(set(nums))[-3]
        