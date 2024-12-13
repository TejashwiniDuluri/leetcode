class Solution:
    def intToRoman(self, num: int) -> str:        
        symbols = ["M", "CM", "D","CD", "C","XC", "L","XL", "X","IX", "V", "IV","I"]
        values = [1000, 900, 500,400, 100,90, 50, 40, 10, 9, 5,4, 1]

        result = ""
        for ind, val in enumerate(values):
            # 1st iteration => 3000, 2000, 1000, 749
            # 2nd iteration => 749, 249
            # 3rd iteration => 

            while num >= val:
                result += symbols[ind]
                num = num - val
        return result
            

num= 3749
obj=Solution()
print(obj.intToRoman(num))

        