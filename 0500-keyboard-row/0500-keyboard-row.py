class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        line1, line2, line3= set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        for word in words:
            w = set(word.lower())
            if w <= line1 or w <= line2 or w <= line3:
                res.append(word)
        return res
        