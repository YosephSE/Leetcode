class Solution:
    def similarPairs(self, words: List[str]) -> int:
        signature_count = Counter()
        for word in words:
            signature_count[''.join(sorted(set(word)))] += 1
        count = 0
        for freq in signature_count.values():
            count += freq * (freq - 1) // 2
        return count
        