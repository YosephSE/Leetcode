class Solution:
    def isAnagram(self,s, t):
        if len(s) != len(t):
            return False
        t = list(t)
        for item in s:
            if item not in t:
                return False
            else:
                t.remove(item)
        return True
        

