class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split()
        for i in range(len(strs)):
            word = list(strs[i])
            l, r = 0, len(word) - 1
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            strs[i] = ''.join(word)
        return ' '.join(strs)


        