class Solution(object):
    def countPrefixSuffixPairs(self, words):
        res = 0
        def isPrefixAndSuffix(str1, str2):
            return str2[:len(str1)] == str1 and str2[len(str2) - len(str1):] == str1
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        return res