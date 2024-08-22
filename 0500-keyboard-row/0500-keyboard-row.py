class Solution:
    def findWords(self, words):
        res = []
        for i in words:
            word = i.lower()
            if re.match("^[qwertyuiop]+$", word) or re.match("^[asdfghjkl]+$", word) or re.match("^[zxcvbnm]+$", word):
                res.append(i)

        return res
        