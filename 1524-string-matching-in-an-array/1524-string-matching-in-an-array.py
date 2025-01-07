class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                elif words[i] in words[j]:
                    res.append(words[i])
        return list(set(res))
        