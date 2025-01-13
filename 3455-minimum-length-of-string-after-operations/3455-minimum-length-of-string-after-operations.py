class Solution(object):
    def minimumLength(self, s):
        freq = Counter(s)
        size = 0
        for i in freq:
            if freq[i] % 2 == 0:
                size += 2
            else:
                size += 1
        return size
        