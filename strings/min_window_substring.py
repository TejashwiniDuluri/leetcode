from collections import defaultdict
class Solution:
    
    #https://www.youtube.com/watch?v=jSto0O4AJbM

    def minWindow(self, s: str, t: str) -> str:
            if t == "":
                  return ""

            t_dict = defaultdict(int)
            s_dict = defaultdict(int)
            
            for ele in t:
                  t_dict[ele] += 1
            have_count = 0
            need_count = len(t_dict)

            min_string_indices, min_string_len = [-1,-1], float("inf")
                        

            l = 0
            for r in range(len(s)):
                
                c = s[r]

                s_dict[c] += 1

                if s_dict[c] == t_dict.get(c,0):
                    have_count += 1                
                
                while have_count == need_count:                    
                    
                    if (r-l+1) < min_string_len:
                        min_string_indices = [l, r]
                        min_string_len = (r-l+1)
                    
                    s_dict[s[l]] -= 1
                    if s_dict.get(s[l]) < t_dict[s[l]]:
                         have_count -= 1
                    l+=1

            l,r = min_string_indices
            
            return s[l:r+1] if min_string_len!= float("inf") else ""
                
obj =Solution()
s = "ADOBECODEBANC"
t = "ABC"
# s ="aa"
# t = "aa"
print(obj.minWindow(s,t))                    

                       

                      

                
                  
                
