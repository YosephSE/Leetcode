class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indexs = {c: i  for i, c in enumerate(order)}
        for j in range(len(words) - 1):
            w1, w2 = words[j], words[j + 1]
            for i in range(len(w1)):
                print(j, i)
                if len(w2) <= i or indexs[w1[i]] > indexs[w2[i]]:
                    return False
                elif indexs[w1[i]] < indexs[w2[i]]:
                    break
        return True

        