class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def binaryConvert(num):
            return bin(num)[2:]
        yy, mm, dd = map(int, date.split('-'))

        return '-'.join([binaryConvert(yy), binaryConvert(mm), binaryConvert(dd)])


        