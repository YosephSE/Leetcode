class Solution:
    def average(self, salary: List[int]) -> float:
        res = 0
        minimum = float('inf')
        maximum = 0

        for i in salary:
            if i > maximum:
                maximum = i
            if i < minimum:
                minimum = i
        for i in salary:
            res += i
        
        return (res - maximum - minimum) / (len(salary) - 2)
        
        