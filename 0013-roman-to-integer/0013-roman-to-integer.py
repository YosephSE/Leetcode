class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        
        result = 0

        
        for i in range(len(s)):
            
            c = s[i]
            value = roman_numerals[c]

            
            if i + 1 < len(s) and roman_numerals[s[i + 1]] > value:
                result -= value

           
            else:
                result += value

    
        return result