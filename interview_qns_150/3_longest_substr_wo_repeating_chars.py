class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_substr = 0
        chars =  set()
        s_len = len(s)

        left = 0

        for right in range(s_len):

            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            
            longest_substr = max(longest_substr, right-left+1)
            chars.add(s[right])
            
        return longest_substr


s = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))