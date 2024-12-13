class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxi = 0
        stack = [-1]
        for i, val in enumerate(s):
            if val == "(":
                stack.append(i)

            else:
                stack.pop()

                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxi = max(maxi, i - stack[-1])
        return maxi


obj = Solution()
s = "(()"  # => 2
# s = ")()())"  # => 4
# s = ")()())()("
# s = "()(())"  # => 6
# s = "))()()"
# s = "()(()"
# s = "(()))())("
s = "()(()"
# s = "(()()"
print(obj.longestValidParentheses(s))