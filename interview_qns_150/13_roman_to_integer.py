class Solution:
    def romanToInt(self, s: str) -> int:
        # di = {
        #     "I" :  1,
        #     "IV" : 4,
        #     "V" :  5,
        #     "IX" : 9,
        #     "X" :  10,
        #     "XL" : 40,
        #     "L" :  50,
        #     "XC" : 90,
        #     "C" :  100,
        #     "CD" : 400,
        #     "D" :  500,
        #     "CM" : 900,
        #     "M" :  1000
        # }
        # s_length = len(s)
        # i = 0
        # result = 0
        # while i < s_length :
            
        #     if s[i:i+2] in di:
        #         result += di.get(s[i:i+2])
        #         i+=2
        #     else:
        #         result += di.get(s[i])
        #         i+=1
            
        # return result            
        di = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s_length = len(s)
        
        res = 0
        for i in range(s_length-1):
            if di.get(s[i]) < di.get(s[i+1]):
                res -= di.get(s[i])
            else:
                res += di.get(s[i])
        
        return res + di.get(s[-1])
    
obj = Solution()
s = "III"
s = "LVIII"
# s = "MCMXCIV"
print(obj.romanToInt(s))