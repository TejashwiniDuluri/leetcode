class Solution:
    
    #https://www.youtube.com/watch?v=tkNWKvxI3mU
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0

        counts = [0] * 26
        longest = 0

        for r in range(len(s)):
            counts[ord(s[r])-65] +=1

            while (r-l+1) - max(counts) > k:
                counts[ord(s[l])-65] -=1
                l+=1
        
            longest = max(longest, (r-l+1))
        
        return longest


            
obj = Solution()
input = "ABAB" 
k = 2
print(obj.characterReplacement(input, k))