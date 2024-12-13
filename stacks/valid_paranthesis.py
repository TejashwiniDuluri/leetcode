class Solution:
    def isValid(self, s: str) -> bool:
        di = {"(": ")", "{": "}", "[": "]"}
        stack = []
        length = 0
        for i in s:
            if di.get(i):
                stack.append(di[i])
                length += 1
            elif length == 0:
                return False
            else:
                removed_element = stack.pop()
                length -= 1
                if removed_element != i:
                    return False
        if length == 0:
            return True
        else:
            return False


obj = Solution()
print(obj.isValid("()[]{}"))
print(obj.isValid("(]"))
print(obj.isValid("()"))
print(obj.isValid(")"))
print(obj.isValid("("))
