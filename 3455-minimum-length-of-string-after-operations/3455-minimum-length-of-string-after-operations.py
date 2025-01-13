class Solution(object):
    def minimumLength(self, s):
        map = {}
        size = len(s)
        for i in s:
            if map.get(i, 0) == 2:
                map[i] -= 1
                size -= 2
            else:
                map[i] = map.get(i, 0) + 1
        return size
        