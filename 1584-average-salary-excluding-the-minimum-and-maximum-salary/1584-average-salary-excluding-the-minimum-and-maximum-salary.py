class Solution:
    def average(self, salary: List[int]) -> float:
        res = 0
        salary.remove(max(salary))
        salary.remove(min(salary))
        for i in salary:
            res += i
        return res / len(salary)
        
        