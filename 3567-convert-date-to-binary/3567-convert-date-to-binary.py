class Solution:
    def convertDateToBinary(self, date: str) -> str:
        yy, mm, dd = map(int, date.split('-'))

        return '-'.join([bin(yy)[2:], bin(mm)[2:], bin(dd)[2:]])


        