class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            val = int(num / 3)
            return [val - 1, val, val + 1]
        return []
        