class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t= list(s), list(t)
        for i in t:
            if i not in s:
                return i
            else:
                s.remove(i)
        return s[0]

        