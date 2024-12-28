class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        dups = set(nums)
        while len(dups) != len(nums) and len(nums) != 0:
            operations += 1
            nums = nums[3:]
            dups =set(nums)
        return operations
 
            
        