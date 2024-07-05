class Solution:
    def isValid(self, s):
        pair = {"(": ")","{": "}","[": "]"}
        stack =[]
        for i in s:
            if i in pair:
                stack.append(i)
            elif len(stack) == 0 or pair[stack.pop()] != i:
                return False
        return len(stack) == 0

        