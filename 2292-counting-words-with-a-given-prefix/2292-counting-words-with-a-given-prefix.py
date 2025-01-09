class Solution(object):
    def prefixCount(self, words, pref):
        n = len(pref)
        count = 0
        for i in words:
            if i[:n] == pref:
                count += 1
        return count