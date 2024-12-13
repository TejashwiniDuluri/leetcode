class Solution:
    def maxDepth(self, s: str) -> int:
        
        depth = 0
        max_depth = 0

        for i in s:
            if i == "(":
                depth += 1                
            elif i == ")":
                max_depth = max(max_depth, depth)                
                depth -= 1
            
        return max_depth

obj = Solution()
s = "(1+(2*3)+((8)/4))+1"
# s = "(1)+((2))+(((3)))"
print(obj.maxDepth(s))
