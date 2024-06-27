class Solution(object):
    def isPalindrome(self, x):
        if ''.join(reversed(str(x))) == str(x):
            return True
        return False