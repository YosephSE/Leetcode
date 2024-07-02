class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for i in address:
            if i == ".":
                res += "[.]"
            else:
                res += i
        return res