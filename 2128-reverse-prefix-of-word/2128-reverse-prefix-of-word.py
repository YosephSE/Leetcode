class Solution(object):
    def reversePrefix(self, word, ch):
        char_index = word.find(ch)
        if char_index == -1:
            return word
        rev = list(word[:char_index + 1])
        rev.reverse()
        res = rev + list(word[char_index + 1:])
        return ''.join(res)

        
        
        return ''.join(res) + word[len(res):]

        