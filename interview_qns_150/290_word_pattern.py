class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ") 
        if len(s) != len(pattern):
            return False
            
        key_map = {}
        val_map = {}
        for i, j in zip(pattern,s):
            print(i, j)
            if key_map.get(i) and key_map.get(i) != j:
                return False
            elif val_map.get(j) and val_map.get(j) != i:
                return False
            else:
                key_map[i] = j
                val_map[j] = i

        return True
    
obj = Solution()
pattern = "abba"
s = "dog cat cat dog"
# pattern = "abba"
# s = "dog cat cat fish"
# pattern ="abba"
# s ="dog dog dog dog"
pattern ="aaa"
s ="aa aa aa aa"
print(obj.wordPattern(pattern, s))
        