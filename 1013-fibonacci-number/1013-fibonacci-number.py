class Solution:
    def fib(self, n: int) -> int:
        seq = [0, 1]
        if n == 0:
            return 0
        for i in range(n - 2):
            seq.append(seq[-1] + seq[-2])

        return seq[-1] + seq[-2]