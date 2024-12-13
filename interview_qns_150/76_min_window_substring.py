from collections import defaultdict

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in t:
            t_dict[i]+=1
        
        need_count = len(t_dict)
        have_count = 0
        s_len = len(s)

        min_sub_str_indices = [-1, -1]
        min_str_len = float("inf")

        left = 0
        for char_index in range(s_len):            
            char = s[char_index]
            
            s_dict[char] +=1

            if t_dict.get(char, 0) == s_dict[char]:
                have_count +=1
            
            while have_count == need_count: # this means along with counts it satisfield all the chars
                #so now take window length = > str length
                window = char_index - left + 1
                if window < min_str_len:
                    min_str_len = window
                    min_sub_str_indices = [left, char_index]

                s_dict[s[left]] -=1
                if s_dict.get(s[left]) < t_dict.get(s[left], 0):
                    have_count -=1
                left+=1
        return s[min_sub_str_indices[0]: min_sub_str_indices[1]+1] if min_str_len != float("inf") else ""


obj = Solution()
s = "ADOBECODEBANC"
t = "ABC"
s = "a"
t = "a"
s = "a"
t = "aa"
print(obj.minWindow(s, t))
