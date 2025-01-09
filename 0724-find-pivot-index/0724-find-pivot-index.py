class Solution(object):
    def pivotIndex(self, nums):
        postfix = [0]
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            total += nums[i]
            postfix.append(total)
        total = 0
        postfix.reverse()
        print(postfix)
        for i in range(len(nums)):
            if total == postfix[i + 1]:
                return i
            total += nums[i]
        return -1
        