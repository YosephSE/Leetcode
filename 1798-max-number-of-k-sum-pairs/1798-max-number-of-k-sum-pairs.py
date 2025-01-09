class Solution(object):
    def maxOperations(self, nums, k):
        oper = 0
        hashMap = {}
        for i in range(len(nums)):
            if k - nums[i] in hashMap:
                oper += 1
                if hashMap[k - nums[i]] > 1:
                    hashMap[k - nums[i]] -= 1
                else:
                    del hashMap[k - nums[i]]
            else:
                hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
        return oper



        
        