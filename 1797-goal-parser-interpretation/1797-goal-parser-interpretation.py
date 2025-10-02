class Solution:
    def interpret(self, command: str) -> str:
        map = {
            "G": "G",
            "()": "o",
            "(al)": "al"
        }
        res = []
        i = 0
        while i < len(command):
            if command[i] == "G":
                i += 1
                res.append("G")
            elif command[i: i + 2] == "()":
                i += 2
                res.append("o")
            elif command[i: i + 4] == "(al)":
                i += 4
                res.append("al")

        return "".join(res)
        