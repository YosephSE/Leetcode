class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            area = (r - l) * min(height[r], height[l])
            maxArea = max(maxArea, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea

