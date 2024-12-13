class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        res = ""
        open = 0
        close = 0
        start = 0
        for i in range(len(s)):

            if s[i] == "(":
                open += 1
            elif s[i] == ")":
                close += 1
            if open == close:
                res += s[start+1 : i]
                start = i+1

        return res




        


s = "(()())(())(()(()))"
obj = Solution()
print(obj.removeOuterParentheses(s))