class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        mapA, mapB = {}, {}
        common = []
        val = 0
        for i in range(len(A)):
            mapA[A[i]] = 1
            mapB[B[i]] = 1
            if A[i] == B[i]:
                val += 1
            else:
                if mapB.get(A[i], 0) == 1:
                    val += 1
                if mapA.get(B[i], 0) == 1:
                    val += 1
            common.append(val)
        return common

            
        
        return common
        