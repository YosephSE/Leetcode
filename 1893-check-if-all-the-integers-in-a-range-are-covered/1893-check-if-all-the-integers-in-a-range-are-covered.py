class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        all_ranges = []
        for i in range(len(ranges)):
            all_ranges.extend(list(range(ranges[i][0], ranges[i][1] + 1)))
        for i in range(left, right + 1):
            if i not in all_ranges:
                return False
        return True



        