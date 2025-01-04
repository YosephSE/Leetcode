class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        maxSum = currSum
        for i in range(1, len(nums) - k + 1):
            currSum -= nums[i - 1]
            currSum += nums[i + k - 1]
            if currSum > maxSum:
                maxSum = currSum
        return maxSum / k


        