class Solution:
    def isValid(self, s: str) -> bool:
        di = {"(": ")", "{": "}", "[": "]"}

        stack = []
        for i in s:
            if di.get(i):
                stack.append(i)
            
            else:
                if not stack:
                    return False
                open_brace = stack.pop()
                if not di.get(open_brace) == i:
                    return False
        
        if stack:
            return False
        return True


obj = Solution()
input = ")([])()"
print(obj.isValid(input))
