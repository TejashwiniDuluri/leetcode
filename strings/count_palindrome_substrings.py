
class Solution:
    def countSubstrings(self, s: str) -> int:
        str_length = len(s)
        count = 0
        
        for i in range(str_length):
            # Odd length palindromes
            low = i
            high = i
            while low >= 0 and high < str_length and s[low] == s[high]:
                count += 1
                low -= 1
                high += 1
                
            # Even length palindromes
            low = i
            high = i + 1
            while low >= 0 and high < str_length and s[low] == s[high]:
                count += 1
                low -= 1
                high += 1
                
        return count
                

            
obj = Solution()
input = "abc"
input = "abba"
print(obj.countSubstrings(input))
            

