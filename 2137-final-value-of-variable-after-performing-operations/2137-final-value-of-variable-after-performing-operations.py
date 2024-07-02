class Solution:
    def finalValueAfterOperations(self, operations):
        sum = 0
        for i in operations:
            if i == "++X" or i == "X++":
                sum += 1
            else:
                sum -= 1
        return sum