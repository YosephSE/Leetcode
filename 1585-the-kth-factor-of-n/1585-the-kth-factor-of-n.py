class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fac = []
        for i in range(1, n // 2 + 1):

            if len(fac) == k:
                return fac[k - 1]
            elif n % i == 0:
                fac.append(i)
        if len(fac) >= k:
            return fac[k-1]
        elif len(fac) == k - 1:
            return n
        return -1
            
            
        