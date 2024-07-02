class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = []
        for i in nums1:
            if i in nums2:
                common.append(i)
                nums2.remove(i)
        return common