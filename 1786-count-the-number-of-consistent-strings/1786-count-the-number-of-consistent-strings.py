class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count = 0
        for word in words:
            is_allowed = True
            for char in word:
                if char not in allowed_set:
                    is_allowed = False
                    break
            if is_allowed:
                count += 1
        return count
                

        