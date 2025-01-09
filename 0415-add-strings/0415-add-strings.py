class Solution(object):
    def addStrings(self, num1, num2):
        l1,l2 = len(num1) - 1, len(num2) - 1
        sum = []
        carry = 0
        while l1 >= 0 or l2 >= 0:
            if l1 >= 0 and l2 >= 0:
                total = ord(num1[l1]) - 48 + ord(num2[l2]) - 48 + carry
            elif l1 >= 0:
                total = ord(num1[l1]) - 48 + carry
            else:
                total = ord(num2[l2]) - 48 + carry
            carry = total // 10
            val = total % 10
            sum.insert(0, chr(val + 48))
            l1 -= 1
            l2 -= 1
        if carry != 0:
            sum.insert(0, chr(carry + 48))
        return ''.join(sum)
        