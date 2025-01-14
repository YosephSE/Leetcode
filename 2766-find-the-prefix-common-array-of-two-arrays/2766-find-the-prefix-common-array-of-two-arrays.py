class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        map = {}
        common = []
        for i in range(len(A)):
            val = len(set(A[:i + 1]).intersection(set(B[:i + 1])))
            common.append(val)
        
        return common
        