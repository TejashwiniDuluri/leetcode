class Solution:

    # GCD is 

    # LCD is

    # a*b / gcd(a,b)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 != str2 + str1:
            return ""
        
        a,b = len(str1), len(str2)

        while b != 0:
            a, b = b, a%b
        
        return str1[0:a]


        
        
    
obj = Solution()
str1 = "ABCABC"
str2 = "ABC"
str1 = "ABABAB"
str2 = "ABAB"
str1 = "AA"
str2 = "A"
str1 ="ABABABAB"
str2 ="ABAB"
str1 ="ABABAB"
str2 ="ABAB"
print(obj.gcdOfStrings(str1, str2))