class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chars = {}
        for i in sentence:
            if i not in chars:
                chars[i] = True
        if len(chars) == 26:
            return True
        return False

        