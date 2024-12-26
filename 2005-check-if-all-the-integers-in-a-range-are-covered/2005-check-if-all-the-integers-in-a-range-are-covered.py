class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            covered = False
            for j in ranges:
                if i in range(j[0], j[1] + 1):
                    covered = True
            if not covered:
                return False
        return True
        