class Solution:
    
    # sliding window approach
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        
        length = len(s)

        longest = 0
        set_list = set()

        for r in range(length):

            while s[r] in set_list:
                set_list.remove(s[l])
                l+=1

            window_size = (r-l) +1
            longest = max(longest, window_size)
            set_list.add(s[r])

        return longest
            

obj = Solution()
input = "abcabcbb"
print(obj.lengthOfLongestSubstring(input) )

        
        