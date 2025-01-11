class Solution:
    def reverse(self, x: int) -> int:
        rev = list(str(x))
        rev = "".join(reversed(rev))
        if rev[-1] == "-":
            rev =  int('-' + rev[:-1])
        else:
            rev = int(rev)
        if -2**31 <= rev <= 2**31 - 1:
            return rev
        return 0

        