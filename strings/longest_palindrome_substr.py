

class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_length = len(s)

        if str_length <= 1:
            return s
        
        longest_palindrome = ""
        palindrome = ""

        
        # odd length strings
        for i in range(1, str_length):
            
            low = i
            high = i

            while s[low] == s[high]:
                low -= 1
                high +=1
                if low < 0 or high >= str_length:
                    break
            
            palindrome = s[low+1 : high]
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome
        
            # even length strings
            low = i-1
            high = i
            
            while s[low] == s[high]:

                low-=1
                high +=1

                if low < 0 or high >= str_length:
                    break

            palindrome = s[low+1 : high]
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome

        return longest_palindrome

obj = Solution()
input = "abbab"
input = "ac"
print(obj.longestPalindrome(input))