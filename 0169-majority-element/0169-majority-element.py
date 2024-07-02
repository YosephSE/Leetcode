class Solution:
    def majorityElement(self, nums):
        dict = {}
        for num in nums:
            dict[num] = 0
        for num in nums:
            dict[num] += 1
        return list(dict.keys())[list(dict.values()).index(max(dict.values()))]

