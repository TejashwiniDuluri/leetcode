from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        chars_len = len(chars)
        
        i = 0        
        write_ptr = 0

        while i < chars_len:
            present = 0
            j = i
            
            while j < chars_len and chars[j] == chars[i]:
                present += 1
                j+=1                

            chars[write_ptr] = chars[i]
            write_ptr +=1

            if present > 1:
                for k in str(present):
                    chars[write_ptr] = k
                    write_ptr +=1
                
            i = j
        return write_ptr


obj = Solution()
chars = ["a","a","b","b","c","c","c"]
chars = ["a", "a", "b"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(obj.compress(chars))