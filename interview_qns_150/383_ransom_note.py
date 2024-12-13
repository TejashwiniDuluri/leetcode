from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rans_counter  = Counter(ransomNote)        
        maga_counter = Counter(magazine)

        for key, val in rans_counter.items():
            if not maga_counter.get(key) or  maga_counter.get(key) < val:
                return False
        return True


        

obj = Solution()
ransomNote = "a"
magazine = "b"
ransomNote = "aa"
magazine = "aab"
print(obj.canConstruct(ransomNote, magazine))