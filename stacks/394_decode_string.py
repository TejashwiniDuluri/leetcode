from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        curr_num = 0
        curr_str = ""

        for i in s:

            if i.isdigit():
                curr_num = curr_num * 10 + int(i)
            
            elif i == "[":

                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            
            elif i == "]":
                last_str,num  = stack.pop()
                curr_str = last_str + curr_str * num
            else:
                curr_str += i
        
        return curr_str

  
obj = Solution()
s = "3[a]2[bc]"
s = "3[a2[c]]"
print(obj.decodeString(s))
