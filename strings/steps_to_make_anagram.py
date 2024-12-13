
from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s_counter = Counter(s)
        t_counter = Counter(t)

        ans_count = 0

        for key, val in s_counter.items():
            
            # print(s_counter.get(key), key)
            if not t_counter.get(key): 
                ans_count += val

            elif val > t_counter.get(key) :                
                ans_count += val - t_counter.get(key) 

            # print(s_counter)
        return ans_count


s = "leetcode"
t = "practice"    
obj = Solution()
print(obj.minSteps(s, t))





        
     

        