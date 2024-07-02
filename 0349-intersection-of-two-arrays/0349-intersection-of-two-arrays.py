class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique = set(nums1)
        res = []
        for i in nums2:
            if i in unique:
                res.append(i)
                unique.remove(i)
        return res
       
