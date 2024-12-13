class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {"a":1, "e":1, "i":1, "o":1,"u":1}
        s_len = len(s)
        
        curr_count = 0
        
        i = 0
        
        while i < k:
            if s[i] in vowels:
                curr_count+=1
            i += 1
        
        max_count = curr_count    
        
        while i < s_len:
            if s[i-k] in vowels:
                curr_count -= 1
            if s[i] in vowels:
                curr_count += 1
            i+=1
            max_count = max(curr_count, max_count)
        
        return max_count
        

    
obj = Solution()
s = "abciiidef"
k = 3
print(obj.maxVowels(s, k))