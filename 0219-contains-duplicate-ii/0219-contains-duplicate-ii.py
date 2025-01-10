class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hash_set = set()
        l, r = 0, 0
        while r < len(nums):
            if nums[r] in hash_set:
                return True
            else:
                hash_set.add(nums[r])
            if r - l < k:
                r += 1
            else:
                hash_set.remove(nums[l])
                r += 1
                l += 1
        return False


        