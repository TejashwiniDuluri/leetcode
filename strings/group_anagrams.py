from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # hash_map = defaultdict(list)
        
        # for i in strs:
        #     counter = [0]*26

        #     for c in i:
        #         counter[ord(c) - 97] +=1
            
        #     hash_map[tuple(counter)].append(i)
        
        # return list(hash_map.values())
        anagrams = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
        
        return list(anagrams.values())
    

obj = Solution()
input = ["eat", "tea", "ate", "bat"]
print(obj.groupAnagrams(input))
  