class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        
        for i in range(len(word1)):
            if i < len(word1):
                res.append(word1[i])
            if i < len(word2):
                res.append(word2[i])
        res.append(word2[len(word1):])
        return ''.join(res)
        