from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # s_count = Counter(s)
        # t_count = Counter(t)

        # print(list(s_count.values()),list(t_count.values()) )
        # if list(s_count.values()) == list(t_count.values()):
        #     return True
        # return False

        key_map = {}
        val_map = {}

        for i, j in zip(s,t):
            if key_map.get(i) and key_map[i] != j:
                return False
            elif val_map.get(j) and val_map[j]!=i:
                return False
            
            key_map[i] = j
            val_map[j] = i
                
        return True


obj =Solution()
s = "egg"
t = "add"
# s = "foo"
# t = "bar"
# s ="bbbaaaba"
# t ="aaabbbba"
# s ="badc"
# t ="baba"

print(obj.isIsomorphic(s, t))
        