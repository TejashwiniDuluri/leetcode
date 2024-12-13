from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     
        # hash_map = defaultdict(list)

        # for word in strs:
        #     curr = [0]*26
        #     for char in word:
        #         curr[ord(char) - 97] = char
        #     hash_map[tuple(curr)].append(word)
        # return list(hash_map.values())

        hash_map = defaultdict(list)
        for word in strs:            
            hash_map[tuple(sorted(word))].append(word)
        return list(hash_map.values())

                





obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(obj.groupAnagrams(strs))