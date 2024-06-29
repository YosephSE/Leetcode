class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n / 2 + 1)):
            print(factors)
            if len(factors) == k:
                return factors[-1]
            elif n % i == 0:
                factors.append(i)
            if len(factors) == k:
                return factors[-1]
        factors.append(n)
        if len(factors) == k:
            return factors[-1]
        return -1