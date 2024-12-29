class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_occur = {}
        for i in s:
            s_occur[i] = s_occur.get(i, 0) + 1
        for i in t:
            if i not in s_occur:
                return i
            s_occur[i] -= 1
        for i in s_occur:
            if s_occur[i] != 0:
                return i
        
            

        