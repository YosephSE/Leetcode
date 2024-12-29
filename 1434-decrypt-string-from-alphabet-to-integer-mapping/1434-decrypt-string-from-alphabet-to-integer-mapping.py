import string
class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        alphabets = {}
        atoi = string.ascii_lowercase
    
        for i in range(len(atoi)):
            if i <= 8:
                alphabets[str(i + 1)] = atoi[i]
            else:
                alphabets[str(i + 1) + '#'] = atoi[i]
            

        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                res.insert(0, alphabets[s[i - 2:i + 1]])
                i -= 3
            else:
                res.insert(0, alphabets[s[i]])
                i -= 1
        return ''.join(res)