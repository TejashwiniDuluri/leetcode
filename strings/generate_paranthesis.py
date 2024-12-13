
class Solution:
    def generateParenthesis(self, n: int) :
 
        result = []

        def backtrack(s = "", open_count=0, close_count=0):
            if len(s) == 2*n:
                result.append(s)
                return
            
            if open_count < n:                
                backtrack(s+"(", open_count+1, close_count)
            
            if close_count < open_count:
                
                backtrack(s+")", open_count, close_count+1)
        
        backtrack()
        return result
    
obj = Solution()
print(obj.generateParenthesis(3))
      
      