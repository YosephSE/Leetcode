class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        occurance = {}
        maxV, maxC = 0, 0
        for char in s:
            occurance[char] = occurance.get(char, 0) + 1
        for i in occurance:
            if i in vowels:
                if occurance[i] > maxV:
                    maxV = occurance[i]
            else:
                if occurance[i] > maxC:
                    maxC = occurance[i]

        return maxV + maxC

        