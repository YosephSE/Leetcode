class Solution:
    def uniqueOccurrences(self, arr):
        res = {}
        for i in arr:
            res[i] = res.get(i, 0) + 1
        return sorted(list(res.values())) == sorted(list(set(res.values())))
        