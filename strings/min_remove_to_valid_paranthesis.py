
class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        
        left_stack = []
        right_stack = []
                
        for i, val in enumerate(s):
            if val == "(":                
                left_stack.append(i)
            elif val == ")":
                if left_stack:
                    left_stack.pop()
                    continue
                else:
                    right_stack.append(i)
                    
                
        result = ""
        stack = left_stack + right_stack
        stack.sort()
        index = None
        
        if stack : 
            index = stack.pop(0)        
        
        for i, char in enumerate(s):               
            if index != None and index == i:            
                if stack:
                    index = stack.pop(0)
                    continue                            
            else:            
                result = result + char 
            
        return result
            
        
        
s = "lee(t(c)o)de)" 
# s = "a)b(c)d"    
# s = "))(("   
obj = Solution()
print(obj.minRemoveToMakeValid(s))