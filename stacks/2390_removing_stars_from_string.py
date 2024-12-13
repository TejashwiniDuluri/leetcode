from typing import List

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if i != "*":
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)

obj = Solution()
s = "leet**cod*e"
print(obj.removeStars(s))
        
