class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            a = 0
            for i in range(1, len(nums)):
                if nums[a] != nums[i]:
                    a += 1
                    nums[a] = nums[i]
            return a + 1