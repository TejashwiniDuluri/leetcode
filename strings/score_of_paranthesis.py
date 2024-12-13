class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        score = 0
        for ele in s:
            if ele == "(":
                stack.append(score)
                score = 0
            else:
                
                score = stack.pop()+ max(2*score, 1)
                
        return score
    


obj =Solution()
s = "()" #=> 1
s = "(())" #=> 2*1
s = "()()" #=> 1+1
s = "(()(()))"  #=> 2 * (1+(2*1))

print(obj.scoreOfParentheses(s))
        