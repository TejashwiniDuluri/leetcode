from typing import List
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_counter = Counter(word1)
        word2_counter = Counter(word2)
        
        if set(word1_counter.keys()) != set(word2_counter.values()):
            return False

        if sorted(word1_counter.values()) != sorted(list(word2_counter.values())):
            return False
        return True


obj = Solution()
word1 = "abc"
word2 = "bca"
word1 = "cabbba"
word2 = "abbccc"
word1 = "abbzccca"
word2 ="babzzczc"
print(obj.closeStrings(word1, word2))
        
